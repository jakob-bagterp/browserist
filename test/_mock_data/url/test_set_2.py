from contextlib import nullcontext as does_not_raise

import pytest
from _mock_data.url.model_2 import URLExpectation, URLTestSet

from browserist.exception.url import URLSyntaxError

VALID_URL = "https://example.com/"

INVALID_URL = "https:/invalid-url"


URL_TEST_SET_DEFAULT = URLTestSet(
    tests=[URLExpectation(VALID_URL, does_not_raise()), URLExpectation(INVALID_URL, pytest.raises(URLSyntaxError))]
)
