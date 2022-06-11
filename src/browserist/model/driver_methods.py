from ..model.browser.base.timeout.strategy import TimeoutStrategy
from .browser.base.driver import BrowserDriver
from .browser.base.settings import BrowserSettings


class DriverMethods:
    """Super class with initializer that can be extended in sub classes for web driver methods."""

    __slots__ = ["_browser_driver", "_driver", "_settings"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        self._browser_driver: BrowserDriver = browser_driver
        self._driver: object = browser_driver.webdriver
        self._settings: BrowserSettings = settings

    def should_continue(self) -> bool:
        """Controller for timeout strategy for each relevant browser method."""
        # TODO: Create unit test.

        return not all([
            self._settings.timeout._is_timed_out,
            self._settings.timeout.strategy is TimeoutStrategy.STOP
        ])

    def set_timed_out(self) -> None:
        """Sets global timeout to true."""
        # TODO: Create unit test.

        self._settings.timeout._is_timed_out = True
