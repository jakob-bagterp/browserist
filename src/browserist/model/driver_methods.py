from .. import helper
from .browser.base.driver import BrowserDriver
from .browser.base.settings import BrowserSettings


class DriverMethods:
    """Super class with initializer that can be extended in sub classes for web driver methods."""

    __slots__ = ["_browser_driver", "_driver", "_settings"]

    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        self._browser_driver: BrowserDriver = browser_driver
        self._driver: object = browser_driver.webdriver
        self._settings: BrowserSettings = settings

    def _should_continue(self) -> bool:
        """Controller for timeout strategy for each relevant browser method."""
        # TODO: Create unit test.

        return helper.timeout.should_continue(self._settings)

    def _mediate_timeout(self, timeout: int | None) -> int:
        """Mediate whether timeout seconds should use a global or a local setting."""
        # TODO: Create unit test.

        return helper.timeout.mediate_timeout(self._settings, timeout)

    def _set_is_timed_out(self) -> None:
        """Sets global timeout to true."""
        # TODO: Create unit test.

        self._settings = helper.timeout.set_is_timed_out(self._settings)
