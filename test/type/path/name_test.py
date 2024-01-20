import os

from browserist.model.type.path import FilePath


def test_file_path_type_get_name() -> None:
    """Test that the FilePath tiny type returns the name of the file or directory."""

    FILE_NAME = "file.txt"
    random_dir_path = os.path.join(os.getcwd(), "random_dir")
    file_path = os.path.join(random_dir_path, FILE_NAME)
    file_path = FilePath(file_path)
    assert file_path.name == FILE_NAME
    assert file_path == os.path.join(random_dir_path, FILE_NAME)
