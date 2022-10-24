from pathlib import Path


def get_path_for_web_mock_data() -> str:
    path_of_this_file = Path(__file__)
    path_of_static_directory = path_of_this_file.parent.parent.resolve()
    return f"{path_of_static_directory}/_mock_data/web"
