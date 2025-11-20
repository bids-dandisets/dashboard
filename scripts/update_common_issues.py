import collections
import json
import os
import pathlib
import warnings

import dandi.dandiapi
import requests
import tabulate2
import tqdm

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)
if GITHUB_TOKEN is None:
    message = "GITHUB_TOKEN environment variable not set"
    raise ValueError(message)

dashboard_directory = pathlib.Path(__file__).parent.parent
common_issues_table_file_path = dashboard_directory / "common_issues_table.md"
content_directory = dashboard_directory / "content"
content_directory.mkdir(exist_ok=True)
common_issues_data_file_path = content_directory / "common_issues_data.json"

client = dandi.dandiapi.DandiAPIClient()
GITHUB_AUTH_HEADER = {"Authorization": f"token {GITHUB_TOKEN}"}

repo_base_url = "https://github.com/bids-dandisets/"
repo_api_base_url = "https://api.github.com/repos/bids-dandisets"
raw_content_base_url = "https://raw.githubusercontent.com/bids-dandisets"

nwb2bids_notifications_file_path = "derivatives/validations/nwb2bids_notifications.json"
bids_validation_file_path = "derivatives/validations/bids_validation.json"

all_responses_per_dandiset = dict()
all_issues_per_source = {
    "nwb2bids_notifications": {"unsanitized": [], "basic_sanitization": []},
    "bids_invalidations": {"unsanitized": [], "basic_sanitization": []},
}

dandisets = list(client.get_dandisets())
for dandiset in tqdm.tqdm(
    iterable=dandisets[:5], total=len(dandisets), desc="Scanning bids-dandisets repos", smoothing=0, unit="Dandiset"
):
    dandiset_id = dandiset.identifier

    repo_api_url = f"{repo_api_base_url}/{dandiset_id}"
    raw_content_url = f"{raw_content_base_url}/{dandiset_id}"
    draft_content_url = f"{raw_content_url}/draft"
    basic_sanitization_content_url = f"{raw_content_url}/basic_sanitization"

    response = requests.get(url=repo_api_url, headers=GITHUB_AUTH_HEADER)
    if response.status_code != 200:
        message = f"Failed to access URL: {repo_api_url} with status code {response.status_code}"
        warnings.warn(message=message)
        continue

    run_info_file_path = f"{draft_content_url}/.nwb2bids/run_info.json"
    response = requests.get(url=run_info_file_path, headers=GITHUB_AUTH_HEADER)
    if response.status_code != 200:
        message = f"Failed to access URL: {run_info_file_path} with status code {response.status_code}"
        warnings.warn(message=message)
        continue

    all_responses_per_dandiset[dandiset_id] = {
        "nwb2bids_notifications": {
            "unsanitized": {"url": f"{draft_content_url}/{nwb2bids_notifications_file_path}", "response": None},
            "basic_sanitization": {
                "url": f"{basic_sanitization_content_url}/{nwb2bids_notifications_file_path}",
                "response": None,
            },
        },
        "bids_invalidations": {
            "unsanitized": {"url": f"{draft_content_url}/{bids_validation_file_path}", "response": None},
            "basic_sanitization": {
                "url": f"{basic_sanitization_content_url}/{bids_validation_file_path}",
                "response": None,
            },
        },
    }

    for source in ["nwb2bids_notifications", "bids_invalidations"]:
        for branch in ["unsanitized", "basic_sanitization"]:
            url = all_responses_per_dandiset[dandiset_id][source][branch]["url"]
            response = requests.get(url=url, headers=GITHUB_AUTH_HEADER)
            all_responses_per_dandiset[dandiset_id][source][branch]["response"] = response

            # Ignore 404 errors for now
            # Corresponds to other problems as seen on main dashboard
            if response.status_code == 404:
                continue

            if response.status_code != 200:
                message = (
                    f"\nFailed to access URL: {url} with status code {response.status_code} "
                    f"and content {response.content}\n\n"
                )
                warnings.warn(message=message)
            else:
                response_json = response.json()

                if source == "nwb2bids_notifications":
                    all_issues_per_source[source][branch].extend(response_json)
                else:
                    all_issues_per_source[source][branch].extend(response_json["issues"]["issues"])

# Aggregate by type
all_issues_by_type = {
    "nwb2bids_notifications": {"unsanitized": dict(), "basic_sanitization": dict()},
    "bids_invalidations": {"unsanitized": dict(), "basic_sanitization": dict()},
}
for source in ["nwb2bids_notifications", "bids_invalidations"]:
    for branch in ["unsanitized", "basic_sanitization"]:
        for issue in all_issues_per_source[source][branch]:
            if source == "nwb2bids_notifications":
                issue_string = f'{issue["category"]} ({issue["severity"]}): {issue["title"]}'
                all_issues_by_type[source][branch][issue_string] = issue
            elif source == "bids_invalidations" and issue["severity"] != "ignore":
                issue_string = f'{issue["severity"].upper()}: {issue["code"]}'
                all_issues_by_type[source][branch][issue_string] = issue

# Count by category and message
issue_counts = {
    "nwb2bids_notifications": {
        "unsanitized": collections.defaultdict(dict),
        "basic_sanitization": collections.defaultdict(dict),
    },
    "bids_invalidations": {
        "unsanitized": collections.defaultdict(dict),
        "basic_sanitization": collections.defaultdict(dict),
    },
}
for source in ["nwb2bids_notifications", "bids_invalidations"]:
    for branch in ["unsanitized", "basic_sanitization"]:
        for issue_string in all_issues_by_type[source][branch]:
            category, message = issue_string.split(":", maxsplit=1)
            issue_counts[source][branch][category][message] = len(all_issues_by_type[source][branch][issue_string])

# Save data to JSON
with common_issues_data_file_path.open(mode="w") as file_stream:
    json.dump(obj=issue_counts, fp=file_stream, indent=2)

# Render markdown table
unique_categories = {
    category for source in issue_counts for branch in issue_counts[source] for category in issue_counts[source][branch]
}
flat_issues_by_source = {
    source: [
        {
            "Severity": category,
            "Message": message,
            "Count (Unsanitized)": issue_counts[source]["unsanitized"].get(category, {}).get(message, 0),
            "Count (Basic sanitization)": issue_counts[source]["basic_sanitization"].get(category, {}).get(message, 0),
        }
        for category in unique_categories
        for message in issue_counts[source]["unsanitized"].get(category, {})
    ]
    for source in issue_counts
    for branch in issue_counts[source]
}

# Sort the lists by descending category (ERROR > WARNING > INFO) and descending total count
for source, flat_issues in flat_issues_by_source.items():
    flat_issues.sort(
        key=lambda issue: (
            {"ERROR": 3, "CRITICAL": 2, "WARNING": 1, "INFO": 0}.get(issue["Severity"].split()[0], -1),
            issue["Count (Unsanitized)"] + issue["Count (Basic sanitization)"],
        ),
        reverse=True,
    )

markdown_table_by_source = {
    source: tabulate2.tabulate(tabular_data=flat_issues, headers="keys", tablefmt="github", colglobalalign="center")
    for source, flat_issues in flat_issues_by_source.items()
}

markdown_lines = [
    "# Common Issues in BIDS Dandisets\n",
    "This table summarizes common issues found in BIDS dandisets processed with nwb2bids.\n",
    "\n\n## BIDS Validator\n",
    markdown_table_by_source["bids_invalidations"],
    "\n\n## `nwb2bids` Notifications\n",
    markdown_table_by_source["nwb2bids_notifications"],
]
markdown_text = "\n".join(markdown_lines)
common_issues_table_file_path.write_text(data=markdown_text)
