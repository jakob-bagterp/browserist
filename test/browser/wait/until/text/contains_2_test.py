from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.homepage import MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.retry import RetryTimeoutException
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize(
    "xpath, regex, expectation",
    [
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "Learn more", does_not_raise()),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "LeARn mOrE", does_not_raise()),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "more", does_not_raise()),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, r"^more", pytest.raises(RetryTimeoutException)),
        (MINI_SITE_HOMEPAGE_BUTTON_FEATURE_1_XPATH, "no valid text", pytest.raises(RetryTimeoutException)),
        (does_not_exist.XPATH, "element doesn't exist", pytest.raises(WaitForElementTimeoutException)),
    ],
)
def test_wait_until_text_contains(xpath: str, regex: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        _ = browser.wait.until.text.contains(xpath, regex, timeout.VERY_SHORT) is not None
