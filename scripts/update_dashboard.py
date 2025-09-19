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
    "# BIDS-Dandisets Dashboard",
    "",
    "A simple dashboard for displaying the successes or failures of running nwb2bids on a Dandiset.",
    "",
]
table_data = []

repo_base_url = "https://github.com/bids-dandisets/"
repo_api_base_url = "https://api.github.com/repos/bids-dandisets"
raw_content_base_url = "https://raw.githubusercontent.com/bids-dandisets"

nwb2bids_inspection_file_path = "draft/derivatives/inspections/nwb2bids_inspection.json"
nwb_inspection_file_path = "draft/derivatives/inspections/src-nwb-inspector_ver-0-6-5.txt"  # TODO: figure out dynamic
bids_validation_file_path = "draft/derivatives/inspections/bids_validation.txt"
bids_validation_json_file_path = "draft/derivatives/inspections/bids_validation.json"
dandi_validation_file_path = "draft/derivatives/inspections/dandi_validation.txt"

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
        row["`nwb2bids` Version"] = "❌"
        row["`nwb2bids` Inspection"] = "❌"
        row["BIDS Validation"] = "❌"
        row["NWB Inspection"] = "❌"
        row["DANDI Validation"] = "❌"
        table_data.append(row)
        continue
    row["Dandiset (BIDS)"] = f"[{dandiset_id}]({repo_base_url}/{dandiset_id})"

    run_info_file_path = f"{raw_content_base_url}/{dandiset_id}/draft/.run_info.json"
    response = requests.get(url=run_info_file_path, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids` Version"] = "❌"
    else:
        previous_run_info = response.json()
        previous_nwb2bids_version_tag = previous_run_info["nwb2bids_version_tag"]
        row["`nwb2bids` Version"] = f"`{previous_nwb2bids_version_tag}`"

    inspection_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb2bids_inspection_file_path}"
    response = requests.get(url=inspection_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids` Inspection"] = "❌"
    else:
        row["`nwb2bids` Inspection"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{nwb2bids_inspection_file_path})"
    # TODO: look at content to determine pass[green]/warning

    bids_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_file_path}"
    response1 = requests.get(url=bids_validation_content_url, headers=github_auth_header)
    bids_validation_json_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_json_file_path}"
    response2 = requests.get(url=bids_validation_json_content_url, headers=github_auth_header)
    if response1.status_code != 200 and response2.status_code != 200:
        row["BIDS Validation"] = "❌"
    else:
        bids_validation = response2.json()
        issues = bids_validation.get("issues", dict()).get("issues",[])
        bids_validation_text = "✅"
        if len(issues) > 0:
            errors = [issue for issue in issues if issue.get("severity", "") == "error"]
            errors_text = f"❌{len(errors)} Errors"
            warnings = [issue for issue in issues if issue.get("severity","") == "warning"]
            warnings_text = f"⚠️{len(warnings)} Warnings"
            if len(errors) > 0 and len(warnings) > 0:
                bids_validation_text = f"{errors_text}<br>{warnings_text}"
            elif len(errors) > 0:
                bids_validation_text = errors_text
            elif len(warnings) > 0:
                bids_validation_text = warnings_text
        row["BIDS Validation"] = f"[{bids_validation_text}]({repo_base_url}/{dandiset_id}/blob/{bids_validation_file_path})"

    nwb_inspection_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb_inspection_file_path}"
    response = requests.get(url=nwb_inspection_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["NWB Inspection"] = "❌"
    else:
        row["NWB Inspection"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{nwb_inspection_file_path})"
    # TODO: look at content to determine pass[green]/warning

    dandi_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{dandi_validation_file_path}"
    response = requests.get(url=dandi_validation_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["DANDI Validation"] = "❌"
    else:
        row["DANDI Validation"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{dandi_validation_file_path})"
    # TODO: look at content to determine pass[green]/warning

    table_data.append(row)

readme_lines += ["### Summary"]
total = len(table_data)
converted_count = sum(1 for row in table_data if "❌" not in row["Dandiset (BIDS)"])
passing_nwb2bids_count = sum(1 for row in table_data if "❌" not in row["`nwb2bids` Inspection"])
passing_bids_count = sum(1 for row in table_data if "❌" not in row["BIDS Validation"])
summary_data = [{
    "Dandisets Successfully Converted": f"{converted_count} / {total} ({converted_count/total:0.1f}%)",
    "Passing `nwb2bids` Inspection": f"{passing_nwb2bids_count} / {converted_count} ({passing_nwb2bids_count/converted_count:0.1f}%)",
    "Passing BIDS Validation": f"{passing_bids_count} / {converted_count} ({passing_bids_count/total:0.1f}%)"
}]
summary_table = tabulate2.tabulate(tabular_data=summary_data, headers="keys", tablefmt="github", colglobalalign="center")
summary_table_lines = summary_table.splitlines()
readme_lines += summary_table_lines

readme_lines += ["### Dandisets"]
full_table = tabulate2.tabulate(tabular_data=table_data, headers="keys", tablefmt="github", colglobalalign="center")
full_table_lines = full_table.splitlines()
readme_lines += full_table_lines

readme_file_path.write_text(data="\n".join(readme_lines), encoding="utf-8")
with table_data_file_path.open(mode="w") as file_stream:
    json.dump(obj=table_data, fp=file_stream, indent=2)
