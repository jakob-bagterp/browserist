from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url
from _helper.xpath.test_set import INVALID_XPATH, VALID_XPATH

from browserist.exception.xpath import XPathSyntaxError
from browserist.model.combo_settings.search import SearchSettings


@pytest.mark.parametrize("xpath1, xpath2, xpath3, expectation", [
    (VALID_XPATH, VALID_XPATH, VALID_XPATH, does_not_raise()),
    (INVALID_XPATH, VALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, INVALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (INVALID_XPATH, INVALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, VALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    (INVALID_XPATH, VALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, INVALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    (INVALID_XPATH, INVALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
])
def test_xpath_exception_handling_of_search_settings(xpath1: str, xpath2: str, xpath3: str, expectation: Any) -> None:
    with expectation:
        _ = SearchSettings(
            input_xpath=xpath1,
            button_xpath=xpath2,
            url=internal_url.EXAMPLE_COM,
            await_search_results_url=internal_url.EXAMPLE_COM,
            await_search_results_xpath=xpath3
        ) is not None
