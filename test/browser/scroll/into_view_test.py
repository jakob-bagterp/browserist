from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.feature_1 import (MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH,
                                                  MINI_SITE_FEATURE_1_IMAGE_1_XPATH)

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("xpath", [
    (MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH),
    (MINI_SITE_FEATURE_1_IMAGE_1_XPATH),
    ("//*[@id='main']/h2[2]"),
    ("//footer"),
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_into_view(xpath: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    browser.scroll.to_position(1, 1)
    x_default, y_default = browser.scroll.get.position()
    browser.scroll.into_view(xpath, timeout.VERY_SHORT)
    x_scrolled, y_scrolled = browser.scroll.get.position()
    assert x_default == x_scrolled == 0
    assert y_default < y_scrolled


@pytest.mark.parametrize("xpath, expectation", [
    (MINI_SITE_FEATURE_1_IMAGE_1_XPATH, does_not_raise()),
    (does_not_exist.XPATH, pytest.raises(WaitForElementTimeoutException)),
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_into_view_timeout(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.MINI_SITE_FEATURE_1)
        browser.scroll.into_view(xpath, timeout.VERY_SHORT)
