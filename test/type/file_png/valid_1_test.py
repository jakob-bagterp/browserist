from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.file_png.test_set_1 import INVALID_PNG_FILE_NAME, VALID_PNG_FILE_NAME

from browserist.exception.file_png import FilePNGSyntaxError
from browserist.model.type.file_png import FilePNG


@pytest.mark.parametrize(
    "file_name, expectation, is_valid_expectation",
    [(VALID_PNG_FILE_NAME, does_not_raise(), True), (INVALID_PNG_FILE_NAME, pytest.raises(FilePNGSyntaxError), False)],
)
def test_file_png_type_is_valid(file_name: str, expectation: Any, is_valid_expectation: bool) -> None:
    with expectation:
        file_name = FilePNG(file_name)
        assert file_name.is_valid() == is_valid_expectation
