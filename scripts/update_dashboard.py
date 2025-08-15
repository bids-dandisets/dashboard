import pathlib

import dandi.dandiapi

dashboard_directory = pathlib.Path(__file__).parent.parent
dandisets_directory = dashboard_directory / "dandisets"
readme_file_path = dashboard_directory / "README.md"

padding = (10, 15)
readme_content = [
    "# nwb2bids Dandisets Dashboard",
    "",
    "A simple dashboard for displaying the successes or failures of running nwb2bids on a Dandiset.",
    "",
    f"| {'Dandiset ID':<{padding[0]}} | {'Status':<{padding[1]}} |",
    f"| :{"-" * padding[0]}: | :{"-" * padding[1]}: |",
]
client = dandi.dandiapi.DandiAPIClient()

for dandiset in client.get_dandisets():
    dandiset_id = dandiset.identifier
    dandiset_directory = dandisets_directory / dandiset_id

    status_file_path = dandiset_directory / "status.txt"
    if status_file_path.exists():
        status_content = status_file_path.read_text().strip()
        status_url = f"https://github.com/con/nwb2bids-dandisets-dashboard/blob/main/dandisets/{dandiset_id}/status.txt"
        status = "Success" if status_content == "Success" else f"[Failed]({status_url})"
        readme_content += [f"| {dandiset_id:<{padding[0]}} | {status:<{padding[1]}} |"]
    else:
        readme_content += [f"| {dandiset_id:<{padding[0]}} | {'Waiting...':<{padding[1]}} |"]
