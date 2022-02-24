from . import directory

_mock_data_directory = directory.get_path_for_static_mock_data()

EXAMPLE_COM: str = f"file://{_mock_data_directory}/example_com.html"

W3SCHOOLS_COM: str = f"file://{_mock_data_directory}/w3schools_com.html"

W3SCHOOLS_COM_DIR: str = f"file://{_mock_data_directory}/w3schools_com_files"
