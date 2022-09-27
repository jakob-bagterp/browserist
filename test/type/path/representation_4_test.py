from _helper.type import validate_representation_file_path
from _mock_data.path.test_set_4 import VALID_FILE_PATH, VALID_PATH, VALID_ROOT_DIR_AS_STRING

from browserist.model.type.path import FilePath


def test_file_path_type_representation_with_path_as_input() -> None:
    """Test that the FilePath tiny type represents itself as a string."""

    validate_representation_file_path(FilePath, VALID_PATH)


def test_file_path_type_representation_with_file_path_as_input() -> None:
    """Test that the FilePath tiny type represents itself as a string."""

    validate_representation_file_path(FilePath, VALID_FILE_PATH)


def test_file_path_type_representation_with_string_as_input() -> None:
    """Test that the FilePath tiny type accepts and converts a directory string as input and a represents itself as a string."""

    validate_representation_file_path(FilePath, VALID_ROOT_DIR_AS_STRING)
