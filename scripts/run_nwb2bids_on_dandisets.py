import pathlib
import traceback

import dandi.dandiapi
import nwb2bids

LIMIT = 1

dashboard_directory = pathlib.Path(__file__).parent.parent
dandisets_directory = dashboard_directory / "dandisets"
dandisets_directory.mkdir(exist_ok=True)

client = dandi.dandiapi.DandiAPIClient()

for counter, dandiset in enumerate(client.get_dandisets()):
    if counter >= LIMIT:
        break

    dandiset_id = dandiset.identifier
    dandiset_directory = dandisets_directory / dandiset_id
    dandiset_directory.mkdir(exist_ok=True)

    status_file_path = dandiset_directory / "status.txt"
    if dandiset_directory.exists() and status_file_path.exists():
        continue

    try:
        dataset_converter = nwb2bids.DatasetConverter.from_remote_dandiset(dandiset_id="000003")
        dataset_converter.extract_metadata()
        status_file_path.write_text(data="Success")
    except Exception as exception:
        status_file_path.write_text(
            data=f"Failed to convert dandiset {dandiset_id}: {exception}\n\nTraceback:\n{traceback.format_exc()}"
        )
