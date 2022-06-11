from typing import Any

from ..model.browser.base.timeout.strategy import TimeoutStrategy
from ..model.type.callable import BrowserMethodCallable
from .browser.base.driver import BrowserDriver
from .browser.base.settings import BrowserSettings


class DriverMethods:
    """Super class with initializer that can be extended in sub classes for web driver methods."""

    __slots__ = ["_browser_driver", "_driver", "_settings"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        self._browser_driver: BrowserDriver = browser_driver
        self._driver: object = browser_driver.webdriver
        self._settings: BrowserSettings = settings

    def timeout_controller(self, browser_method: BrowserMethodCallable, timeout: int | None) -> Any:
        """Handles timeout settings for each relevant browser method."""

        if self._settings.timeout._is_timed_out and self._settings.timeout.strategy is TimeoutStrategy.STOP:
            return
        if timeout is None:
            timeout = self._settings.timeout.seconds
        return browser_method(..., timeout=timeout)

    def set_timed_out(self) -> None:
        """Sets global timeout to true."""

        self._settings.timeout._is_timed_out = True
