from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _config.browser_settings import default
from _mock_data.url import internal_url

from browserist import Browser, BrowserSettings
from browserist.constant import timeout
from browserist.exception.headless import MethodNotSupportedInHeadlessModeException


@pytest.mark.parametrize("browser_settings, expectation", [
    (default.DEFAULT, does_not_raise()),
    (default.HEADLESS, pytest.raises(MethodNotSupportedInHeadlessModeException)),
])
def test_headless_mode_in_select_input_field_exceptions(browser_settings: BrowserSettings, expectation: Any) -> None:
    with Browser(browser_settings) as browser:
        with expectation:
            browser.open.url(internal_url.EXAMPLE_COM)
            browser.input.select("/html/body/div/p[2]/a", timeout.VERY_SHORT)
