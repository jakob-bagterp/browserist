from _helper.type import validate_bypass
from _mock_data.path.test_set_4 import VALID_PATH, VALID_ROOT_DIR_AS_STRING

from browserist.model.type.path import FilePath


def test_file_path_type_bypass_if_already_file_path_with_path() -> None:
    """Test that if an input already is a validated FilePath element, bypass and don't create a new object."""

    validate_bypass(FilePath, VALID_PATH)


def test_file_path_type_bypass_if_already_file_path_with_string() -> None:
    """Test that if an input already is a validated FilePath element, bypass and don't create a new object."""

    validate_bypass(FilePath, VALID_ROOT_DIR_AS_STRING)
