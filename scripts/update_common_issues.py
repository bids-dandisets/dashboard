import os
import pathlib
import warnings

import dandi.dandiapi
import requests
import tqdm

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)
if GITHUB_TOKEN is None:
    message = "GITHUB_TOKEN environment variable not set"
    raise ValueError(message)

dashboard_directory = pathlib.Path(__file__).parent.parent
dandisets_directory = dashboard_directory / "dandisets"
readme_file_path = dashboard_directory / "README.md"
full_table_file_path = dashboard_directory / "full_table.md"
content_directory = dashboard_directory / "content"
content_directory.mkdir(exist_ok=True)
table_data_file_path = content_directory / "table_data.json"

client = dandi.dandiapi.DandiAPIClient()
GITHUB_AUTH_HEADER = {"Authorization": f"token {GITHUB_TOKEN}"}

readme_lines = [
    "# BIDS-Dandisets Dashboard",
    "A simple dashboard for displaying the successes or failures of running `nwb2bids` on all Dandisets.",
]
table_data = []

repo_base_url = "https://github.com/bids-dandisets/"
repo_api_base_url = "https://api.github.com/repos/bids-dandisets"
raw_content_base_url = "https://raw.githubusercontent.com/bids-dandisets"

nwb2bids_notifications_file_path = "derivatives/validations/nwb2bids_notifications.json"
bids_validation_file_path = "derivatives/validations/bids_validation.json"

responses_per_dandiset = dict()
all_issues_per_source = {
    "nwb2bids_notifications": [],
    "bids_invalidations": [],
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

    responses_per_dandiset[dandiset_id] = {
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
            url = responses_per_dandiset[dandiset_id][source][branch]["url"]
            response = requests.get(url=url, headers=GITHUB_AUTH_HEADER)
            responses_per_dandiset[dandiset_id][source][branch]["response"] = response

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
                all_issues_per_source[source] += response_json

a = 1
