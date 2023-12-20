from .. import helper
from .browser.base.driver import BrowserDriver


class DriverMethods:
    """Super class with initializer that can be extended in sub classes for web driver methods."""

    __slots__ = ["_browser_driver"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        self._browser_driver: BrowserDriver = browser_driver

    def _timeout_should_continue(self) -> bool:
        """Controller for timeout strategy for each relevant browser method."""

        return helper.timeout.should_continue(self._browser_driver.settings)

    def _mediate_timeout(self, timeout: float | None) -> float:
        """Mediate whether timeout seconds should use a global or a local setting."""

        return helper.timeout.mediate_timeout(self._browser_driver.settings, timeout)

    def _mediate_idle_download_timeout(self, idle_download_timeout: float | None) -> float:
        """Mediate whether idle download seconds should use a global or a local setting."""

        return helper.timeout.mediate_idle_download_timeout(self._browser_driver.settings, idle_download_timeout)

    def _set_is_timed_out(self) -> None:
        """Sets global timeout to true."""

        self._browser_driver.settings = helper.timeout.set_is_timed_out(self._browser_driver.settings)
