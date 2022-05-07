from abc import ABC, abstractmethod

from ..base.driver import BrowserDriver


class BrowserExtension(ABC):
    """Abstract class that contains the extension methods for certain browser types."""

    __slots__ = ["browser_driver"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        self.browser_driver = browser_driver

    @abstractmethod
    def enable_images(self) -> None:
        """Intended use: Revert disabled images for a browser when its web driver doesn't support a session-based configuration for Selenium, but only a global configuration that impacts normal use."""
