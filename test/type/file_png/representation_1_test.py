from _mock_data.file_png.test_set_1 import VALID_PNG_FILE_NAME

from browserist.model.type.file_png import FilePNG


def test_file_png_type_representation() -> None:
    """Test that the XPath tiny type represents itself as a an URL string."""

    file_png_input = expected_file_png_output = VALID_PNG_FILE_NAME
    file_png_type = FilePNG(file_png_input)
    assert expected_file_png_output == file_png_type
    assert expected_file_png_output == file_png_type.value
