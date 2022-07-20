from contextlib import nullcontext as does_not_raise

import pytest
from _mock_data.file_png.model_1 import FilePNGExpectation, FilePNGTestSet

from browserist.exception.file_png import FilePNGSyntaxError

VALID_PNG_FILE_NAME = "image_file.png"

INVALID_PNG_FILE_NAME = "image_file.jpg"


FILE_PNG_TEST_SET_DEFAULT = FilePNGTestSet(
    tests=[
        FilePNGExpectation(file_name=VALID_PNG_FILE_NAME, expectation=does_not_raise()),
        FilePNGExpectation(file_name=INVALID_PNG_FILE_NAME, expectation=pytest.raises(FilePNGSyntaxError)),
    ]
)
