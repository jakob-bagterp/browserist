from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url.test_set_2 import INVALID_URL, VALID_URL

from browserist.exception.url import URLSyntaxError
from browserist.model.type.url import URL


@pytest.mark.parametrize(
    "url, expectation", [(VALID_URL, does_not_raise()), (INVALID_URL, pytest.raises(URLSyntaxError))]
)
def test_url_type_exception_handling(url: str, expectation: Any) -> None:
    with expectation:
        _ = URL(url) is not None
