import pathlib

import dandi.dandiapi

dashboard_directory = pathlib.Path(__file__).parent.parent
dandisets_directory = dashboard_directory / "dandisets"
readme_file_path = dashboard_directory / "README.md"

readme_lines = [
    "# nwb2bids Dandisets Dashboard",
    "",
    "A simple dashboard for displaying the successes or failures of running nwb2bids on a Dandiset.",
    "",
]
client = dandi.dandiapi.DandiAPIClient()

dandiset_ids = []
statuses = []
for dandiset in client.get_dandisets():
    dandiset_id = dandiset.identifier

    inspection_content_url = f"https://raw.githubusercontent.com/bids-dandisets/{dandiset_id}/"

    dandiset_directory = dandisets_directory / dandiset_id
    dandiset_directory.mkdir(exist_ok=True)

    status_file_path = dandiset_directory / "status.txt"
    if status_file_path.exists():
        status_content = status_file_path.read_text().strip()
        status_url = f"https://github.com/con/nwb2bids-dandisets-dashboard/blob/main/dandisets/{dandiset_id}/status.txt"
        status = "Success" if status_content == "Success" else f"[Failed]({status_url})"
    else:
        status = "Not processed"

    dandiset_ids.append(dandiset_id)
    statuses.append(status)

content_json = {
    "data": {
        "Dandiset ID": [dandiset.identifier for dandiset in client.get_dandisets()],
        "Status": [
            "Success" if (dandisets_directory / dandiset.identifier / "status.txt").read_text().strip() == "Success"
            else "Failed"
            for dandiset in client.get_dandisets()
        ],
    },
}

padding = (10, 15)
readme_lines += json_to_markdown_table(json_table=content_json, padding=padding)

readme = "\n".join(readme_lines)
readme_file_path.write_text(data=readme)

# TODO: move this to a standalone package
def json_to_markdown_table(json_table: dict, *, padding: tuple[int, ...] | None = None) -> list[str]:
    """
    Convert a JSON object to a Markdown table.

    Parameters
    ----------
    json_table : dict
        The JSON data to convert.

    Returns
    -------
    str
        A string representing the Markdown table.

    Examples
    --------
    json_table = {
        "title": "My Example Table",
        "subtitle": "This is a subtitle.",
        "headers": ["My header 1.", "My header 2."],
        "tails": ["This is a tail.", "This is another tail."],
        "data": {
             "Name": ["Alice", "Bob", "Charlie"],
             "Age": [30, 25, 35],
             "City": ["New York", "Los Angeles", "Chicago"]
         }
    }

    print(json_to_markdown_table(json_table=json_table))
    >>> # My Example Table

    # This is a subtitle.

    My header 1.
    My header 2.

    | Name    | Age | City         |
    | :---: | :---: | :----: |
    | Alice   | 30  | New York     |
    | Bob     | 25  | Los Angeles  |
    | Charlie | 35  | Chicago      |

    This is a tail.
    This is another tail.
    """
    title = json_table.get("title", None)
    subtitle = json_table.get("subtitle", None)
    headers = json_table.get("headers", None)
    tails = json_table.get("tails", None)

    data = json_table["data"]
    column_names = list(data.keys())
    rows: list[list[str, ...]] = [list(row) for row in zip(*(data[column_name] for column_name in column_names))]

    if padding is None:
        padding = tuple(
            max(len(column_name), max(len(str(value)) for value in [column_name] + [row[column_index] for row in rows]))
            for column_index, column_name in enumerate(column_names)
        )

    markdown_table = []
    if title is not None:
        markdown_table += [f"# {title}", ""]
    if subtitle is not None:
        markdown_table += [f"## {subtitle}", ""]
    if headers is not None:
        markdown_table += headers
        markdown_table += [""]
    formatted_column_names = [
        f"{column_name:<{padding[column_index]}}" for column_index, column_name in enumerate(column_names)
    ]
    markdown_table += ["| " + " | ".join(formatted_column_names) + " |"]
    formatted_dashes = [":" + "-" * (padding[column_index] - 2) + ":" for column_index in range(len(column_names))]
    markdown_table += ["| " + " | ".join(formatted_dashes) + " |"]
    for row in rows:
        markdown_table += [
            "| " + " | ".join(f"{value:<{padding[column_index]}}" for column_index, value in enumerate(row)) + " |"
        ]
    if tails is not None:
        markdown_table += [""]
        markdown_table += tails

    return markdown_table