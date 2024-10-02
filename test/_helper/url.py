from pathlib import Path


def convert_internal_url_to_file_path(url: str) -> Path:
    url_as_file_path = url.replace("file://", "", 1)
    return Path(rf"{url_as_file_path}")
