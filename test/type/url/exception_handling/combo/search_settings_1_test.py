from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url.test_set_2 import INVALID_URL, VALID_URL
from _mock_data.xpath.constant import VALID_XPATH

from browserist.exception.url import URLSyntaxError
from browserist.model.combo_settings.search import SearchSettings


@pytest.mark.parametrize(
    "url, expectation", [(VALID_URL, does_not_raise()), (INVALID_URL, pytest.raises(URLSyntaxError))]
)
def test_url_exception_handling_of_search_settings(url: str, expectation: Any) -> None:
    with expectation:
        _ = (
            SearchSettings(
                input_xpath=VALID_XPATH,
                button_xpath=VALID_XPATH,
                url=url,
                await_search_results_url_contains=VALID_URL,
                await_search_results_xpath=VALID_XPATH,
            )
            is not None
        )
