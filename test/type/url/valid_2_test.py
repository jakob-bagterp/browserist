from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url.test_set_2 import INVALID_URL, VALID_URL

from browserist.exception.url import URLSyntaxError
from browserist.model.type.url import URL


@pytest.mark.parametrize(
    "url, expectation, is_valid_expectation",
    [(VALID_URL, does_not_raise(), True), (INVALID_URL, pytest.raises(URLSyntaxError), False)],
)
def test_url_type_is_valid(url: str, expectation: Any, is_valid_expectation: bool) -> None:
    with expectation:
        url = URL(url)
        assert url.is_valid() == is_valid_expectation
