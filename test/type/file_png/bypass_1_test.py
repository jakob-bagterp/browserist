from _helper.type import validate_bypass
from _mock_data.file_png.test_set_1 import VALID_PNG_FILE_NAME

from browserist.model.type.file_png import FilePNG


def test_file_png_type_bypass_if_already_png_file() -> None:
    """Test that if an input already is a validated FilePNG element, bypass and don't create a new object."""

    validate_bypass(FilePNG, VALID_PNG_FILE_NAME)
