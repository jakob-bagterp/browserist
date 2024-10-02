from pathlib import Path


def convert_internal_url_to_file_path(url: str) -> Path:
    url_as_file_path = url.replace("file://", "", 1)
    root_dir = Path(__file__).parent.parent.parent.resolve()
    return Path.joinpath(root_dir, url_as_file_path)
