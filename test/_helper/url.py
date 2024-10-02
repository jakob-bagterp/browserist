from pathlib import Path


def convert_internal_url_to_file_path(url: str) -> Path:
    return Path(url.replace("file://", ""))
