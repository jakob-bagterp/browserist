from _helper import directory

from browserist.helper.directory import update_path_format_if_windows

_web_mock_data_directory = directory.get_path_for_web_mock_data()

EXAMPLE_COM: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/example_com.html")

W3SCHOOLS_COM: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/w3schools_com.html")

W3SCHOOLS_COM_DIR: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/w3schools_com_files")
