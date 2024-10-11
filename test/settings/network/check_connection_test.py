import contextlib
from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _fixture.internet_connection import NetworkDisabler
from _mock_data.url import internal_url
from urllib3.exceptions import ProtocolError

from browserist import Browser, BrowserSettings

BROWSER_SETTINGS_WITH_CHECK_CONNECTION = BrowserSettings(
    headless=True,
    disable_images=True,
    check_connection=True
)

BROWSER_SETTINGS_WITHOUT_CHECK_CONNECTION = BrowserSettings(
    headless=True,
    disable_images=True,
    check_connection=False
)


@pytest.mark.parametrize("browser_settings, expectation", [
    (BROWSER_SETTINGS_WITH_CHECK_CONNECTION, pytest.raises(ConnectionError)),
    (BROWSER_SETTINGS_WITHOUT_CHECK_CONNECTION, does_not_raise()),
])
def test_check_connection_exception_handling_without_internet(browser_settings: BrowserSettings, expectation: Any) -> None:
    with NetworkDisabler():
        with contextlib.suppress(ProtocolError):  # Now that we have disabled the network in the socket, we need to ignore ProtocolError when making connection requests.
            with expectation:
                _ = Browser(browser_settings) is not None

    # Test that the connection is enabled again after disabling it in the above test:
    browser_settings = BrowserSettings(headless=True)
    with Browser(browser_settings) as browser:
        browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
        heading = browser.get.text("//h1")
        assert heading == "Welcome"
