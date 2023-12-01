from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
import requests
from pytest import MonkeyPatch

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
def test_check_connection_exception_handling_without_internet(browser_settings: BrowserSettings, expectation: Any, monkeypatch: MonkeyPatch) -> None:
    def emulate_no_internet_connection():
        raise requests.exceptions.RequestException("No internet connection")

    with expectation:
        monkeypatch.setattr(requests, "get", emulate_no_internet_connection)
        _ = Browser(browser_settings) is not None
