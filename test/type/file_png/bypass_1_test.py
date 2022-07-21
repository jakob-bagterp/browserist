from _mock_data.file_png.test_set_1 import VALID_PNG_FILE_NAME

from browserist.model.type.file_png import FilePNG


def test_file_png_type_bypass_if_already_png_file() -> None:
    """Test that if an input already is a validated FilePNG element, bypass and don't create a new object."""

    url_type = FilePNG(VALID_PNG_FILE_NAME)
    assert url_type is FilePNG(url_type)
    assert FilePNG(VALID_PNG_FILE_NAME) is not FilePNG(VALID_PNG_FILE_NAME)
