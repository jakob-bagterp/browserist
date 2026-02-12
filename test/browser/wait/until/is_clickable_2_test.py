from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import (
    MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH,
    MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH,
)

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize(
    "xpath, expectation",
    [
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, does_not_raise()),
        (MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH, does_not_raise()),
        (does_not_exist.XPATH, pytest.raises(RetryTimeoutException)),
    ],
)
def test_wait_until_element_is_clickable(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        _ = browser.wait.until.is_clickable(xpath, timeout.VERY_SHORT) is not None
