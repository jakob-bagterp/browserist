import contextlib
from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _fixture.internet_connection import NetworkDisabler
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import ProtocolError

from browserist import Browser, BrowserSettings

BROWSER_SETTINGS_WITH_CHECK_CONNECTION = BrowserSettings(headless=True, disable_images=True, check_connection=True)

BROWSER_SETTINGS_WITHOUT_CHECK_CONNECTION = BrowserSettings(headless=True, disable_images=True, check_connection=False)


@pytest.mark.parametrize(
    "browser_settings, expectation",
    [
        (BROWSER_SETTINGS_WITH_CHECK_CONNECTION, pytest.raises(ConnectionError)),
        (BROWSER_SETTINGS_WITHOUT_CHECK_CONNECTION, does_not_raise()),
    ],
)
def test_check_connection_exception_handling_without_internet(
    browser_settings: BrowserSettings, expectation: Any
) -> None:
    with NetworkDisabler():
        with contextlib.suppress(
            ProtocolError, OSError, WebDriverException
        ):  # Now that we have disabled the network in the socket, we need to ignore ProtocolError when making connection requests.
            with expectation:
                _ = Browser(browser_settings) is not None
