from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException


@pytest.mark.parametrize(
    "xpath, expectation",
    [
        (does_not_exist.XPATH, pytest.raises(RetryTimeoutException)),
        (MINI_SITE_HOMEPAGE_HEADLINE_H1_XPATH, does_not_raise()),
    ],
)
def test_wait_until_element_contains_any_text(xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        _ = browser.wait.until.contains_any_text(xpath, timeout.VERY_SHORT) is not None
