import contextlib
from collections.abc import Generator
from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
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
def test_check_connection_exception_handling_without_internet(browser_settings: BrowserSettings, expectation: Any, disable_network: Generator[None, None, None]) -> None:
    with contextlib.suppress(ProtocolError):  # Now that we have disabled the network in the socket, we need to ignore ProtocolError when making connection requests.
        with expectation:
            _ = Browser(browser_settings) is not None
