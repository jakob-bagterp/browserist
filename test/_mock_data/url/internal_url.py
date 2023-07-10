from _helper import directory

from browserist.helper.directory import update_path_format_if_windows

_web_mock_data_directory = directory.get_path_for_web_mock_data()

CHECKBOXES: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/checkboxes.html")

DROPDOWN_SELECTOR: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/drop-down_selector.html")

EXAMPLE_COM: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/example_com.html")

NO_BODY: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/no_body.html")

RADIO_BUTTONS: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/radio_buttons.html")

SCROLL_CANVAS: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/scroll_canvas.html")

W3SCHOOLS_COM: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/w3schools_com.html")

W3SCHOOLS_COM_DIR: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/w3schools_com_files")
