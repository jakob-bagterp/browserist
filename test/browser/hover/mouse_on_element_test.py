from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("xpath, expectation", [
    ("/html/body/div/p[2]/a", does_not_raise()),
    ("/html/body/div/h1/div", pytest.raises(WaitForElementTimeoutException)),
])
def test_hover_mouse_on_element(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.EXAMPLE_COM)
    with expectation:
        browser.hover.mouse_on_element(xpath, timeout.VERY_SHORT) is not None
