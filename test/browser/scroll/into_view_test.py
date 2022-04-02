from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("xpath", [
    ("//*[@id='main']/div[2]/div/div[1]/h1"),
    ("//*[@id='Frontend']/img"),
    ("//*[@id='main']/div[6]/div/div[2]/div/h3"),
])
def test_scroll_into_view(xpath: str, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    browser.open.url(internal_url.W3SCHOOLS_COM)
    browser.scroll.to_position(1, 1)
    x_default, y_default = browser.scroll.get_position()
    browser.scroll.into_view(xpath, timeout.VERY_SHORT)
    x_scrolled, y_scrolled = browser.scroll.get_position()
    assert x_default == x_scrolled == 0 and y_default < y_scrolled


@pytest.mark.parametrize("xpath, expectation", [
    ("//*[@id='Frontend']/img", does_not_raise()),
    ("//*[@id='Frontend']/img/div", pytest.raises(WaitForElementTimeoutException)),
])
def test_scroll_into_view_timeout(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(internal_url.W3SCHOOLS_COM)
        browser.scroll.into_view(xpath, timeout.VERY_SHORT)
