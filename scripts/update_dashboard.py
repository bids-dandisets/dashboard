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
full_table_file_path = dashboard_directory / "full_table.md"
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
basic_sanitization_nwb2bids_notifications_file_path = (
    "basic_sanitization/derivatives/validations/nwb2bids_notifications.json"
)
# nwb_inspection_file_path = "draft/derivatives/validations/src-nwb-inspector_ver-0-6-5.txt"
bids_validation_file_path = "draft/derivatives/validations/bids_validation.txt"
bids_validation_json_file_path = "draft/derivatives/validations/bids_validation.json"
basic_sanitization_bids_validation_file_path = "basic_sanitization/derivatives/validations/bids_validation.txt"
basic_sanitization_bids_validation_json_file_path = "basic_sanitization/derivatives/validations/bids_validation.json"
# dandi_validation_file_path = "draft/derivatives/validations/dandi_validation.txt"

MODALITY_SHORT_MAP = {
    "electrophysiological approach": "ephys",
    "behavioral approach": "beh",
    "microscopy approach; cell population imaging": "micr",
    "optogenetic approach": "ogen",
}
SOURCE_SHIELD_URL = "https://img.shields.io/badge/Source-blue?logo=github"
SOURCE_SHIELD_MD = "![](https://img.shields.io/badge/Source-blue?logo=github)"
BIDS_SHIELD_URL = "https://img.shields.io/badge/BIDS-blue?logo=github"
BIDS_SHIELD_MD = "![](https://img.shields.io/badge/BIDS-blue?logo=github)"
BASIC_SANITIZATION_SHIELD_MD = "![](https://img.shields.io/badge/Sanitized-blue?logo=github)"
BIDS_VALIDATION_UNSANITIZED_KEY = (
    "BIDS ([BEP32](https://bids.neuroimaging.io/extensions/beps/bep_032.html))<br>Validation<br>(Unsanitized)"
)
BIDS_VALIDATION_BASIC_SANITIZATION_KEY = (
    "BIDS ([BEP32](https://bids.neuroimaging.io/extensions/beps/bep_032.html))<br>Validation<br>(Basic Sanitization)"
)

dandisets = list(client.get_dandisets())
for dandiset in tqdm.tqdm(
    iterable=dandisets[:30], total=len(dandisets), desc="Scanning bids-dandisets repos", smoothing=0, unit="Dandiset"
):
    dandiset_id = dandiset.identifier

    row = dict()
    row["Dandiset ID"] = "1"

    raw_metadata = dandiset.get_raw_metadata()
    row["Dandiset<br>Modalities"] = "<br>".join(
        [
            MODALITY_SHORT_MAP.get(approach_name := approach.get("name", ""), approach_name.removesuffix(" approach"))
            for approach in raw_metadata.get("assetsSummary", dict()).get("approach", [])
        ]
    )

    # TODO: skip update based on commit hash or other etag

    repo_api_url = f"{repo_api_base_url}/{dandiset_id}"
    response = requests.get(url=repo_api_url, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Version"] = "❗"
        row["`nwb2bids`<br>Notifications<br>(Unsanitized)"] = "❗"
        row[BIDS_VALIDATION_UNSANITIZED_KEY] = "❗"
        row["`nwb2bids`<br>Notifications<br>(Basic Sanitization)"] = "❗"
        row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY] = "❗"
        # row["NWB Inspection"] = "❗"  # NWB Inspections may not make sense for this repo (on existing Dandisets)
        # row["DANDI Validation"] = "❗"  # DANDI Validation requires integration of BEP32 and others
        table_data.append(row)
        continue
    row["Dandiset ID"] = (
        f"{dandiset_id}"
        f'<br><a href="https://dandiarchive.org/dandiset/{dandiset_id}"><img src="https://raw.githubusercontent.com/'
        f'dandi/dandi-archive/master/web/public/favicon.ico" width="16" height="16"/></a>'
        f"<br>[{SOURCE_SHIELD_MD}](https://github.com/dandisets/{dandiset_id})"
    )

    run_info_file_path = f"{raw_content_base_url}/{dandiset_id}/draft/.nwb2bids/run_info.json"
    response = requests.get(url=run_info_file_path, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Version"] = "❗Missing"
        row["Status<br>(Unsanitized)"] = "❗Missing"
    else:
        row["Dandiset ID"] += f"<br>[{BIDS_SHIELD_MD}]({repo_base_url}/{dandiset_id})"

        run_info = response.json()

        nwb2bids_version = run_info["nwb2bids_version"]
        row["`nwb2bids`<br>Version"] = f"`{nwb2bids_version}`"

        sessions_converted_text = "No<br>sessions<br>converted"
        if run_info["total_sessions"] == "???":
            row["Status<br>(Unsanitized)"] = f"Session(s): {run_info["sessions_converted"]}/???"
        elif str(run_info["total_sessions"]).endswith("+"):
            row["Status<br>(Unsanitized)"] = (
                f"Session(s): {run_info["sessions_converted"]}/{run_info["total_sessions"]}"
            )
        elif run_info["total_sessions"] == 0:
            row["Status<br>(Unsanitized)"] = "Session(s): 0/0"
        elif run_info["total_sessions"] > 0:
            row["Status<br>(Unsanitized)"] = (
                f"Session(s): {run_info["sessions_converted"]}/{run_info["total_sessions"]} "
                f"({run_info["sessions_converted"]/int(run_info["total_sessions"])*100:0.1f}%)"
            )

        manifest_file_path = f"{raw_content_base_url}/{dandiset_id}/draft/.nwb2bids/manifest.txt"
        response = requests.get(url=manifest_file_path, headers=github_auth_header)
        if response.status_code == 200:
            manifest = response.content.decode(encoding="utf-8")
            filenames = [line.strip() for line in manifest.splitlines() if line != "\n"]

            filenames_by_type = dict()
            for suffix in [".nwb", ".tsv", ".json"]:
                if suffix == ".nwb":
                    filenames_by_type[suffix] = [filename for filename in filenames if filename.endswith(suffix)]
                    continue

                for key in ["participant", "session", "probe", "electrode", "channel"]:
                    key_files = [filename for filename in filenames if filename.endswith(suffix) and key in filename]
                    filenames_by_type[f"{key}{suffix}"] = key_files

            file_count_by_type = {key: len(value) for key, value in filenames_by_type.items()}

            row["Status<br>(Unsanitized)"] += f'<br>NWB file(s): {file_count_by_type[".nwb"]}'
            for key in ["participant", "session", "probe", "electrode", "channel"]:
                tsv_count = file_count_by_type[f"{key}.tsv"]
                json_count = file_count_by_type[f"{key}.json"]

                if tsv_count == json_count and tsv_count == 0:
                    continue

                row["Status<br>(Unsanitized)"] += f"<br>{key.capitalize()} files: {tsv_count} .tsv {json_count} .json"

    # Parse detailed nwb2bids notifications
    nwb2bids_notifications_content_url = f"{raw_content_base_url}/{dandiset_id}/{nwb2bids_notifications_file_path}"
    response = requests.get(url=nwb2bids_notifications_content_url, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Notifications<br>(Unsanitized)"] = "❗Missing"
    else:
        nwb2bids_notifications = response.json()

        already_bids = (
            issue for issue in nwb2bids_notifications if issue.get("title", "") == "Dandiset is already BIDS"
        )
        if any(already_bids):
            row["Dandiset ID"] = dandiset_id
            row["Status<br>(Unsanitized)"] = "⏭️Skipped (already BIDS)"
            row[BIDS_VALIDATION_UNSANITIZED_KEY] = ""
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

        row["`nwb2bids`<br>Notifications<br>(Unsanitized)"] = (
            f"[{nwb2bids_notifications_text}]({repo_base_url}/{dandiset_id}/blob/{nwb2bids_notifications_file_path})"
        )

    # Parse detailed BIDS validation results (unsanitized)
    if "0 NWB" in row["Status<br>(Unsanitized)"]:
        row[BIDS_VALIDATION_UNSANITIZED_KEY] = "⏭️Skipped"
        row["`nwb2bids`<br>Notifications<br>(Basic Sanitization)"] = "️⏭️"
        row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY] = "⏭️Skipped"
        table_data.append(row)
        continue

    bids_validation_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_file_path}"
    content_response = requests.get(url=bids_validation_content_url, headers=github_auth_header)
    bids_validation_json_content_url = f"{raw_content_base_url}/{dandiset_id}/{bids_validation_json_file_path}"
    json_response = requests.get(url=bids_validation_json_content_url, headers=github_auth_header)
    if content_response.status_code != 200 or json_response.status_code != 200:
        row[BIDS_VALIDATION_UNSANITIZED_KEY] = "❗Missing"
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

        row[BIDS_VALIDATION_UNSANITIZED_KEY] = (
            f"[{bids_validation_text}]({repo_base_url}/{dandiset_id}/blob/{bids_validation_file_path})"
        )

    # Basic Sanitization
    basic_sanitization_run_info_file_path = (
        f"{raw_content_base_url}/{dandiset_id}/basic_sanitization/.nwb2bids/run_info.json"
    )
    response = requests.get(url=basic_sanitization_run_info_file_path, headers=github_auth_header)
    if response.status_code != 200:
        row["`nwb2bids`<br>Notifications<br>(Basic Sanitization)"] = "❗Missing"
        row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY] = "❗Missing"
    else:
        row[
            "Dandiset ID"
        ] += f"<br>[{BASIC_SANITIZATION_SHIELD_MD}]({repo_base_url}/{dandiset_id}/tree/basic_sanitization)"

    basic_sanitization_nwb2bids_notifications_content_url = (
        f"{raw_content_base_url}/{dandiset_id}/{basic_sanitization_nwb2bids_notifications_file_path}"
    )
    response = requests.get(url=basic_sanitization_nwb2bids_notifications_content_url, headers=github_auth_header)
    if response.status_code == 200:
        nwb2bids_notifications = response.json()

        already_bids = (
            issue for issue in nwb2bids_notifications if issue.get("title", "") == "Dandiset is already BIDS"
        )
        if any(already_bids):
            row["`nwb2bids`<br>Notifications<br>(Basic Sanitization)"] = "⏭️"
            row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY] = "⏭️"
            table_data.append(row)
            continue

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

        blob_url = f"{repo_base_url}/{dandiset_id}/blob/{basic_sanitization_nwb2bids_notifications_file_path}"
        row["`nwb2bids`<br>Notifications<br>(Basic Sanitization)"] = f"[{nwb2bids_notifications_text}]({blob_url})"

    # Parse detailed BIDS validation results (basic sanitization)
    bids_validation_content_url = (
        f"{raw_content_base_url}/{dandiset_id}/{basic_sanitization_bids_validation_json_file_path}"
    )
    content_response = requests.get(url=bids_validation_content_url, headers=github_auth_header)
    bids_validation_json_content_url = (
        f"{raw_content_base_url}/{dandiset_id}/{basic_sanitization_bids_validation_json_file_path}"
    )
    json_response = requests.get(url=bids_validation_json_content_url, headers=github_auth_header)
    if content_response.status_code != 200 or json_response.status_code != 200:
        row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY] = "❗Missing"
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

        blob_url = f"{repo_base_url}/{dandiset_id}/blob/{basic_sanitization_bids_validation_file_path}"
        row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY] = f"[{bids_validation_text}]({blob_url})"

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

    if row["`nwb2bids`<br>Notifications<br>(Unsanitized)"] == "Skipped (already BIDS)" or "BIDS" in row["Dandiset ID"]:
        run_on_count += 1

passing_nwb2bids_unsanitized_count = sum(
    1
    for row in table_data
    if "❌" not in row["`nwb2bids`<br>Notifications<br>(Unsanitized)"]
    and "❗" not in row["`nwb2bids`<br>Notifications<br>(Unsanitized)"]
)
passing_nwb2bids_basic_sanitization_count = sum(
    1
    for row in table_data
    if "❌" not in row["`nwb2bids`<br>Notifications<br>(Unsanitized)"]
    and "❗" not in row["`nwb2bids`<br>Notifications<br>(Unsanitized)"]
)
passing_bids_unsanitized_count = sum(
    1
    for row in table_data
    if "❌" not in row[BIDS_VALIDATION_UNSANITIZED_KEY] and "❗" not in row[BIDS_VALIDATION_UNSANITIZED_KEY]
)
passing_bids_basic_sanitization_count = sum(
    1
    for row in table_data
    if "❌" not in row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY]
    and "❗" not in row[BIDS_VALIDATION_BASIC_SANITIZATION_KEY]
)

if run_on_count == 0:
    nwb2bids_inspection_unsanitized_summary_text = (
        f"{passing_nwb2bids_unsanitized_count}/{run_on_count} "
        f"({passing_nwb2bids_unsanitized_count / total * 100:0.1f}%)"
    )
    summary_entry = {
        BIDS_VALIDATION_UNSANITIZED_KEY: (
            f"{passing_bids_unsanitized_count}/{run_on_count} ({passing_bids_unsanitized_count / total * 100:0.1f}%)"
        ),
    }
else:
    nwb2bids_inspection_unsanitized_summary_text = (
        f"{passing_nwb2bids_unsanitized_count}/{run_on_count} "
        f"({passing_nwb2bids_unsanitized_count / run_on_count * 100:0.1f}%)"
    )
    nwb2bids_inspection_basic_sanitization_summary_text = (
        f"{passing_nwb2bids_basic_sanitization_count}/{run_on_count} "
        f"({passing_nwb2bids_basic_sanitization_count / run_on_count * 100:0.1f}%)"
    )
    _key1 = "Passing<br>`nwb2bids`<br>Notifications<br>(Basic sanitization)"
    summary_entry = {
        "Latest<br>version": latest_version,
        "Run on<br>latest<br>version": f"{run_on_count}/{total} ({run_on_count / total * 100:0.1f}%)",
        "Passing<br>`nwb2bids`<br>Notifications<br>(Unsanitized)": nwb2bids_inspection_unsanitized_summary_text,
        f"Passing<br>{BIDS_VALIDATION_UNSANITIZED_KEY}": (
            f"{passing_bids_unsanitized_count}/{run_on_count} "
            f"({passing_bids_unsanitized_count / run_on_count * 100:0.1f}%)"
        ),
        _key1: nwb2bids_inspection_basic_sanitization_summary_text,
        f"Passing<br>{BIDS_VALIDATION_BASIC_SANITIZATION_KEY}": (
            f"{passing_bids_basic_sanitization_count}/{run_on_count} "
            f"({passing_bids_unsanitized_count / run_on_count * 100:0.1f}%)"
        ),
    }

summary_data = [summary_entry]
summary_table = tabulate2.tabulate(
    tabular_data=summary_data, headers="keys", tablefmt="github", colglobalalign="center"
)
summary_table_lines = summary_table.splitlines()
readme_lines += summary_table_lines

readme_lines += ["### Full Table"]
readme_lines += ["To see the results without any skips removed, go to the [Full Table](./full_table.md)."]
full_table = tabulate2.tabulate(tabular_data=table_data, headers="keys", tablefmt="github", colglobalalign="center")
full_table_lines = full_table.splitlines()
full_table_file_path.write_text(data="\n".join(full_table_lines), encoding="utf-8")

readme_lines += ["### Dandisets"]
unskipped_lines = [
    line for line in full_table_lines if "Skipped" not in line and "0/0" not in line and line.count("Missing") < 3
]
readme_lines += unskipped_lines

readme_file_path.write_text(data="\n".join(readme_lines), encoding="utf-8")
with table_data_file_path.open(mode="w") as file_stream:
    json.dump(obj=table_data, fp=file_stream, indent=2)
