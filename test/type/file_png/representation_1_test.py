from _helper.type import validate_representation
from _mock_data.file_png.test_set_1 import VALID_PNG_FILE_NAME

from browserist.model.type.file_png import FilePNG


def test_file_png_type_representation() -> None:
    """Test that the FilePNG tiny type represents itself as a string."""

    validate_representation(FilePNG, VALID_PNG_FILE_NAME)
