from . import BrowserExtension
from ....helper import browser_factory

class SafariBrowserExtension(BrowserExtension):
    def enable_images(self) -> None:
        """Intended use: Revert disabled images for Safari as its web driver doesn't support a session-based configuration for Selenium, but only a global configuration that impacts normal use."""

        browser_factory.safari.enable_images(self.browser_driver)
