from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _config.browser_settings import default
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser, BrowserSettings
from browserist.constant import timeout
from browserist.exception.headless import MethodNotSupportedInHeadlessModeException


@pytest.mark.parametrize(
    "browser_settings, expectation",
    [(default.DEFAULT, does_not_raise()), (default.HEADLESS, pytest.raises(MethodNotSupportedInHeadlessModeException))],
)
def test_headless_mode_in_select_input_field_exceptions(browser_settings: BrowserSettings, expectation: Any) -> None:
    with Browser(browser_settings) as browser:
        with expectation:
            browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
            browser.input.select(MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, timeout.VERY_SHORT)
