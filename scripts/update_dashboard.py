import json
import os
import pathlib

import dandi.dandiapi
import requests
import tabulate2
import tqdm

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", None)
if GITHUB_TOKEN is None:
    message = "GITHUB_TOKEN environment variable not set"
    raise ValueError(message)

dashboard_directory = pathlib.Path(__file__).parent.parent
dandisets_directory = dashboard_directory / "dandisets"
readme_file_path = dashboard_directory / "README.md"
content_directory = dashboard_directory / "content"
content_directory.mkdir(exist_ok=True)
table_data_file_path = content_directory / "table_data.json"

client = dandi.dandiapi.DandiAPIClient()
github_auth_header = {"Authorization": f"token {GITHUB_TOKEN}"}

readme_lines = [
    "# nwb2bids Dandisets Dashboard",
    "",
    "A simple dashboard for displaying the successes or failures of running nwb2bids on a Dandiset.",
    "",
]
table_data = []

repo_base_url = "https://github.com/bids-dandisets/"
repo_api_base_url = "https://api.github.com/repos/bids-dandisets"
raw_content_base_url = "https://raw.githubusercontent.com/bids-dandisets"

nwb2bids_inspection_file_path = "draft/derivatives/inspections/nwb2bids_inspection_results.json"
nwb_inspection_file_path = "draft/derivatives/inspections/nwb_inspection.json"
bids_validation_file_path = "draft/derivatives/inspections/bids_validation.json"
dandi_validation_file_path = "draft/derivatives/inspections/dandi_validation.json"

dandisets = list(client.get_dandisets())
for dandiset in tqdm.tqdm(
    iterable=dandisets, total=len(dandisets), desc="Scanning bids-dandisets repos", smoothing=0, unit="Dandiset"
):
    dandiset_id = dandiset.identifier

    row = dict()
    row["Dandiset ID"] = dandiset_id

    # TODO: skip update based on commit hash or other etag

    repo_api_url = f"{repo_api_base_url}/{dandiset_id}"
    response = requests.get(url=repo_api_url, headers=github_auth_header)
    if response.status_code != 200:
        row["Dandiset (BIDS)"] = "❌"
        row["nwb2bids hash"] = "❌"
        row["nwb2bids Inspection"] = "❌"
        row["NWB Inspection"] = "❌"
        row["BIDS Validation"] = "❌"
        row["DANDI Validation"] = "❌"
        continue
    row["Dandiset (BIDS)"] = f"[{dandiset_id}]({repo_base_url}/{dandiset_id})"

    nwb2bids_hash_content_url = f"{raw_content_base_url}/{dandiset_id}/draft/.nwb2bids_commit_hash"
    response = requests.get(url=nwb2bids_hash_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["nwb2bids hash"] = "❌"
    else:
        row["nwb2bids hash"] = f"`{response.text.strip()}`"

    inspection_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb2bids_inspection_file_path}"
    response = requests.get(url=inspection_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["nwb2bids Inspection"] = "❌"
    else:
        row["nwb2bids Inspection"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{nwb2bids_inspection_file_path})"
    # TODO: look at content to determine pass[green]/warning

    nwb_inspection_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb_inspection_file_path}"
    response = requests.get(url=nwb_inspection_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["NWB Inspection"] = "❌"
    else:
        row["NWB Inspection"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{nwb_inspection_file_path})"
    # TODO: look at content to determine pass[green]/warning

    bids_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_file_path}"
    response = requests.get(url=bids_validation_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["BIDS Validation"] = "❌"
    else:
        row["BIDS Validation"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{bids_validation_file_path})"
    # TODO: look at content to determine pass[green]/warning

    dandi_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{dandi_validation_file_path}"
    response = requests.get(url=dandi_validation_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["DANDI Validation"] = "❌"
    else:
        row["DANDI Validation"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{dandi_validation_file_path})"
    # TODO: look at content to determine pass[green]/warning

    table_data.append(row)

markdown_table = tabulate2.tabulate(tabular_data=table_data, headers="keys", tablefmt="github", numalign="center")
markdown_lines = markdown_table.splitlines()
readme_lines += markdown_lines

readme_file_path.write_text(data="\n".join(readme_lines), encoding="utf-8")
with table_data_file_path.open(mode="w") as file_stream:
    json.dump(obj=table_data, fp=file_stream, indent=4)
