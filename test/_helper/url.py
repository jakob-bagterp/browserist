def convert_internal_url_to_file_path(url: str) -> str:
    return url.replace("file://", "")
