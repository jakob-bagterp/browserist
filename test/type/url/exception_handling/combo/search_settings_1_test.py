from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.url.test_set_1 import INVALID_URL, VALID_URL
from _helper.xpath.test_set_2 import VALID_XPATH

from browserist.exception.url import URLSyntaxError
from browserist.model.combo_settings.search import SearchSettings


@pytest.mark.parametrize("url1, url2, expectation", [
    (VALID_URL, VALID_URL, does_not_raise()),
    (INVALID_URL, VALID_URL, pytest.raises(URLSyntaxError)),
    (VALID_URL, INVALID_URL, pytest.raises(URLSyntaxError)),
    (INVALID_URL, INVALID_URL, pytest.raises(URLSyntaxError)),
])
def test_url_exception_handling_of_search_settings(url1: str, url2: str, expectation: Any) -> None:
    with expectation:
        _ = SearchSettings(
            input_xpath=VALID_XPATH,
            button_xpath=VALID_XPATH,
            url=url1,
            await_search_results_url=url2,
            await_search_results_xpath=VALID_XPATH
        ) is not None
