from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url import internal_url

from browserist import Browser
from browserist.constant import timeout
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("url, xpath, expectation", [
    (internal_url.W3SCHOOLS_COM, "//img", does_not_raise()),
    (internal_url.EXAMPLE_COM, "//img", pytest.raises(WaitForElementTimeoutException)),
])
def test_wait_until_images_have_loaded(url: str, xpath: str, expectation: Any, browser_default_headless: Browser) -> None:
    browser = browser_default_headless
    with expectation:
        browser.open.url(url)
        browser.wait.until.images_have_loaded(xpath, timeout.VERY_SHORT) is not None
