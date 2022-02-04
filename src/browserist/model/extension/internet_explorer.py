from ...helper import internet_explorer
from .base import BrowserExtension

class InternetExplorerBrowserExtension(BrowserExtension):
    def enable_images(self) -> None:
        """Intended use: Revert disabled images for Internet Explorer as its web driver doesn't support a session-based configuration for Selenium, but only a global configuration that impacts normal use."""

        internet_explorer.enable_images(self.browser_driver)
