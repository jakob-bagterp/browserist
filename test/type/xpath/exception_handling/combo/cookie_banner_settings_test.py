from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url
from _helper.xpath import INVALID_XPATH, VALID_XPATH

from browserist.constant import timeout
from browserist.exception.xpath import XPathSyntaxError
from browserist.model.combo_settings.cookie_banner import CookieBannerSettings


@pytest.mark.parametrize("xpath1, xpath2, expectation", [
    (VALID_XPATH, VALID_XPATH, does_not_raise()),
    (INVALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    (INVALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
])
def test_xpath_exception_handling_of_cookie_bannger_settings(xpath1: str, xpath2: str, expectation: Any) -> None:
    with expectation:
        _ = CookieBannerSettings(
            button_xpath=xpath1,
            url=internal_url.EXAMPLE_COM,
            has_loaded_xpath=xpath2,
            has_disappeared_wait_seconds=timeout.VERY_SHORT
        ) is not None
