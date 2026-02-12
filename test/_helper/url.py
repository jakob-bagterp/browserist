from browserist.helper import operating_system


def convert_internal_url_to_file_path(url: str) -> str:
    url_as_file_path = url.replace("file://", "", 1)
    if operating_system.is_windows():
        url_as_file_path = url_as_file_path.replace("/", "\\")  # Convert slashes to backslashes.
        url_as_file_path = url_as_file_path.replace(
            "\\", "", 1
        )  # Ensure that the first backslash is removed, e.g. from "\\D:\\path\\" to "D:\\path".
    return url_as_file_path
