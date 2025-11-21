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
        # Ignore 404 errors for now
        # Corresponds to other problems as seen on main dashboard
        if response.status_code == 404:
            continue

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
                response_lines = response.text.splitlines()

                if source == "bids_invalidations":
                    human_readable_lines = requests.get(
                        url=url.replace(".json", ".txt"), headers=GITHUB_AUTH_HEADER
                    ).text.splitlines()
                else:
                    human_readable_lines = response_lines

                response_json = (
                    response.json() if source == "nwb2bids_notifications" else response.json()["issues"]["issues"]
                )

                # Mutate issue objects in place to add source urls
                for issue in response_json:
                    if issue.get("severity", "") == "ignore":
                        issue["source_url"] = ""
                        continue

                    source_url = url.replace(raw_content_base_url, repo_base_url + "/").replace(
                        "/draft/", "/blob/draft/"
                    )

                    if source == "bids_invalidations":
                        source_url = source_url.replace(".json", ".txt")
                        matching_index = (
                            next(index for index, line in enumerate(human_readable_lines) if issue["code"] in line) + 1
                        )
                    else:
                        matching_index = (
                            next(index for index, line in enumerate(human_readable_lines) if issue["title"] in line) + 1
                        )
                    issue["source_url"] = f"{source_url}#L{matching_index}"

                all_issues_per_source[source][branch].extend(response_json)

# Aggregate by type
all_issues_by_type = {
    "nwb2bids_notifications": {
        "unsanitized": collections.defaultdict(list),
        "basic_sanitization": collections.defaultdict(list),
    },
    "bids_invalidations": {
        "unsanitized": collections.defaultdict(list),
        "basic_sanitization": collections.defaultdict(list),
    },
}
for source in ["nwb2bids_notifications", "bids_invalidations"]:
    for branch in ["unsanitized", "basic_sanitization"]:
        for issue in all_issues_per_source[source][branch]:
            if source == "nwb2bids_notifications":
                issue_string = f'{issue["category"]} ({issue["severity"]}): {issue["title"]}'
                all_issues_by_type[source][branch][issue_string].append(issue)
            elif source == "bids_invalidations" and issue["severity"] != "ignore":
                issue_string = f'{issue["severity"].upper()}: {issue["code"]}'
                all_issues_by_type[source][branch][issue_string].append(issue)

# Count by category and title
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
            category, title = issue_string.split(": ", maxsplit=1)
            issue_counts[source][branch][category][title] = len(all_issues_by_type[source][branch][issue_string])

# Save data to JSON
with common_issues_data_file_path.open(mode="w") as file_stream:
    json.dump(obj=issue_counts, fp=file_stream, indent=2)

# Render markdown table
unique_categories = {
    category for source in issue_counts for branch in issue_counts[source] for category in issue_counts[source][branch]
}
title_key = {"nwb2bids_notifications": "title", "bids_invalidations": "code"}
unique_titles = {
    issue[title_key[source]]
    for source in all_issues_per_source
    for branch in all_issues_per_source[source]
    for issue in all_issues_per_source[source][branch]
}
example_links_per_title = {
    title: next(
        f'[{title}]({issue["source_url"]})'
        for source in all_issues_per_source
        for branch in all_issues_per_source[source]
        for issue in all_issues_per_source[source][branch]
        if issue[title_key[source]] == title
    )
    for title in unique_titles
}

flat_issues_by_source = {
    source: []
    for source in issue_counts
}
for source in issue_counts:
    for branch in issue_counts[source]:
        for category in unique_categories:
            for title in issue_counts[source][branch].get(category, {}):
                flat_issues_by_source[source].append(
                    {
                        "Severity": category,
                        "Title": example_links_per_title.get(title, title),
                        "Count<br>(Unsanitized)": issue_counts[source]["unsanitized"].get(category, {}).get(title, 0),
                        "Count<br>(Basic sanitization)": issue_counts[source]["basic_sanitization"].get(category, {}).get(title, 0),
                    }
                )

# Sort lists by number of sanitized errors
for source in flat_issues_by_source:
    flat_issues_by_source[source].sort(key=lambda issue: issue["Count<br>(Basic sanitization)"], reverse=True)

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
