import collections
import json
import os
import pathlib

import dandi.dandiapi
import packaging.version
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
    "A simple dashboard for displaying the successes or failures of running `nwb2bids` on all Dandisets.",
]
table_data = []

repo_base_url = "https://github.com/bids-dandisets/"
repo_api_base_url = "https://api.github.com/repos/bids-dandisets"
raw_content_base_url = "https://raw.githubusercontent.com/bids-dandisets"

nwb2bids_notifications_file_path = "draft/derivatives/validations/nwb2bids_notifications.json"
# nwb_inspection_file_path = "draft/derivatives/validations/src-nwb-inspector_ver-0-6-5.txt"
bids_validation_file_path = "draft/derivatives/validations/bids_validation.txt"
bids_validation_json_file_path = "draft/derivatives/validations/bids_validation.json"
# dandi_validation_file_path = "draft/derivatives/validations/dandi_validation.txt"

dandisets = list(client.get_dandisets())
for dandiset in tqdm.tqdm(
    iterable=dandisets, total=len(dandisets), desc="Scanning bids-dandisets repos", smoothing=0, unit="Dandiset"
):
    dandiset_id = dandiset.identifier

    row = dict()
    row["Dandiset ID<br>(BIDS)"] = dandiset_id

    # TODO: skip update based on commit hash or other etag

    repo_api_url = f"{repo_api_base_url}/{dandiset_id}"
    response = requests.get(url=repo_api_url, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Version"] = "❗"
        row["`nwb2bids`<br>Notifications"] = "❗"
        row["BIDS<br>Validation"] = "❗"
        # row["NWB Inspection"] = "❗"
        # row["DANDI Validation"] = "❗"
        table_data.append(row)
        continue
    row["Dandiset ID<br>(BIDS)"] = f"[{dandiset_id}]({repo_base_url}/{dandiset_id})"

    run_info_file_path = f"{raw_content_base_url}/{dandiset_id}/draft/.nwb2bids/run_info.json"
    response = requests.get(url=run_info_file_path, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Version"] = "❗Missing"
        row["Sessions<br>Converted<br>(Unsanitized)"] = "❗Missing"
    else:
        run_info = response.json()

        nwb2bids_version = run_info["nwb2bids_version"]
        row["`nwb2bids`<br>Version"] = f"`{nwb2bids_version}`"

        sessions_converted_text = "No<br>sessions<br>converted"
        if run_info["total_sessions"] != 0:
            row["Sessions<br>Converted<br>(Unsanitized)"] = (
                f"{run_info["sessions_converted"]} / {run_info["total_sessions"]} "
                f"({run_info["sessions_converted"]/run_info["total_sessions"]*100:0.1f}%)"
            )

    # Parse detailed nwb2bids notifications
    nwb2bids_notifications_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb2bids_notifications_file_path}"
    response = requests.get(url=nwb2bids_notifications_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Notifications"] = "❗Missing"
    else:
        nwb2bids_notifications = response.json()

        already_bids = (
            issue for issue in nwb2bids_notifications if issue.get("title", "") == "Dandiset is already BIDS"
        )
        if any(already_bids):
            row["Dandiset ID<br>(BIDS)"] = dandiset_id
            row["Sessions<br>Converted<br>(Unsanitized)"] = "⏭️Skipped (already BIDS)"
            row["BIDS<br>Validation"] = ""
            # row["NWB Inspection"] = ""
            # row["DANDI Validation"] = ""

        nwb2bids_notifications_text = "✅"
        if len(nwb2bids_notifications) > 0:
            notifications_by_severity = collections.defaultdict(list)
            for notification in nwb2bids_notifications:
                severity = notification["severity"]
                match severity:
                    case "ERROR":
                        notifications_by_severity["ERROR"].append(notification)
                    case "CRITICAL":
                        notifications_by_severity["CRITICAL"].append(notification)
                    case "WARNING" | "INFO" | "DEBUG":
                        notifications_by_severity["SUGGESTION"].append(notification)

            nwb2bids_notifications_lines = []
            if len(errors := notifications_by_severity["ERROR"]) > 0:
                plural = "s" if (count := len(errors)) > 1 else ""
                nwb2bids_notifications_lines.append(f"❌{count} Error{plural}")
            if len(criticals := notifications_by_severity["CRITICAL"]) > 0:
                plural = "s" if (count := len(criticals)) > 1 else ""
                nwb2bids_notifications_lines.append(f"🔶{count} Critical{plural}")
            if len(suggestions := notifications_by_severity["SUGGESTION"]) > 0:
                plural = "s" if (count := len(suggestions)) > 1 else ""
                nwb2bids_notifications_lines.append(f"⚠️{count} Suggestion{plural}")
            nwb2bids_notifications_text = "<br>".join(nwb2bids_notifications_lines)

        row["`nwb2bids`<br>Notifications"] = (
            f"[{nwb2bids_notifications_text}]({repo_base_url}/{dandiset_id}/blob/{nwb2bids_notifications_file_path})"
        )

    # Parse detailed BIDS validation results
    bids_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_file_path}"
    content_response = requests.get(url=bids_validation_content_url, headers=github_auth_header)
    bids_validation_json_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_json_file_path}"
    json_response = requests.get(url=bids_validation_json_content_url, headers=github_auth_header)
    if content_response.status_code != 200 or json_response.status_code != 200:
        row["BIDS<br>Validation"] = "❗Missing"
    else:
        bids_validation = json_response.json()
        issues = bids_validation.get("issues", dict()).get("issues", [])

        bids_validation_text = "✅"
        if len(issues) > 0:
            issues_by_severity = collections.defaultdict(list)
            for issue in issues:
                severity = issue["severity"]
                match severity:
                    case "error":
                        issues_by_severity["ERROR"].append(issue)
                    case "warning":
                        issues_by_severity["WARNING"].append(issue)

            bids_validation_lines = []
            if len(errors := issues_by_severity["ERROR"]) > 0:
                plural = "s" if (count := len(errors)) > 1 else ""
                bids_validation_lines.append(f"❌{count} Error{plural}")
            if len(warnings := issues_by_severity["WARNING"]) > 0:
                plural = "s" if (count := len(warnings)) > 1 else ""
                bids_validation_lines.append(f"⚠️{count} Warning{plural}")
            bids_validation_text = "<br>".join(bids_validation_lines)

        row["BIDS<br>Validation"] = (
            f"[{bids_validation_text}]({repo_base_url}/{dandiset_id}/blob/{bids_validation_file_path})"
        )

    # nwb_inspection_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb_inspection_file_path}"
    # response = requests.get(url=nwb_inspection_content_url, headers=github_auth_header)
    # if response.status_code != 200:
    #     row["NWB Inspection"] = "❌"
    # else:
    #     row["NWB Inspection"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{nwb_inspection_file_path})"
    # TODO: look at content to determine pass[green]/warning

    # dandi_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{dandi_validation_file_path}"
    # response = requests.get(url=dandi_validation_content_url, headers=github_auth_header)
    # if response.status_code != 200:
    #     row["DANDI Validation"] = "❌"
    # else:
    #     row["DANDI Validation"] = f"[⚠️]({repo_base_url}/{dandiset_id}/blob/{dandi_validation_file_path})"
    # TODO: look at content to determine pass[green]/warning

    table_data.append(row)

readme_lines += ["### Summary"]
total = len(table_data)
latest_version = max(
    (
        packaging.version.Version(version=(row["`nwb2bids`<br>Version"].split("-")[0].removeprefix("`v")))
        if "❗" not in row["`nwb2bids`<br>Version"]
        else packaging.version.Version("0.0.0")
    )
    for row in table_data
    if row["`nwb2bids`<br>Version"] != "❌"
)

run_on_count = 0
for row in table_data:
    if row["`nwb2bids`<br>Version"] == "❌":
        continue

    version = (
        packaging.version.Version(version=row["`nwb2bids`<br>Version"].split("-")[0].removeprefix("`v"))
        if "❗" not in row["`nwb2bids`<br>Version"]
        else packaging.version.Version("0.0.0")
    )
    if version != latest_version:
        continue

    if row["`nwb2bids`<br>Notifications"] == "Skipped (already BIDS)" or row["Dandiset ID<br>(BIDS)"].startswith("["):
        run_on_count += 1

passing_nwb2bids_count = sum(
    1
    for row in table_data
    if "❌" not in row["`nwb2bids`<br>Notifications"] and "❗" not in row["`nwb2bids`<br>Notifications"]
)
passing_bids_count = sum(
    1 for row in table_data if "❌" not in row["BIDS<br>Validation"] and "❗" not in row["BIDS<br>Validation"]
)

nwb2bids_inspection_summary_text = (
    f"{passing_nwb2bids_count} / {run_on_count} ({passing_nwb2bids_count / run_on_count * 100:0.1f}%)"
)

if run_on_count == 0:
    summary_entry = {
        "Passing<br>BIDS<br>Validation": (
            f"{passing_bids_count} / {run_on_count} ({passing_bids_count / total * 100:0.1f}%)"
        ),
    }
else:
    summary_entry = {
        "Latest<br>version": latest_version,
        "Run on<br>latest<br>version": f"{run_on_count} / {total} ({run_on_count / total * 100:0.1f}%)",
        "Passing<br>`nwb2bids`<br>Notifications<br>(Unsanitized)": nwb2bids_inspection_summary_text,
        "Passing<br>BIDS<br>Validation<br>(Unsanitized)": (
            f"{passing_bids_count} / {run_on_count} ({passing_bids_count / total * 100:0.1f}%)"
        ),
    }

summary_data = [summary_entry]
summary_table = tabulate2.tabulate(
    tabular_data=summary_data, headers="keys", tablefmt="github", colglobalalign="center"
)
summary_table_lines = summary_table.splitlines()
readme_lines += summary_table_lines

readme_lines += ["### Dandisets"]
full_table = tabulate2.tabulate(tabular_data=table_data, headers="keys", tablefmt="github", colglobalalign="center")
full_table_lines = full_table.splitlines()
readme_lines += full_table_lines

readme_file_path.write_text(data="\n".join(readme_lines), encoding="utf-8")
with table_data_file_path.open(mode="w") as file_stream:
    json.dump(obj=table_data, fp=file_stream, indent=2)
