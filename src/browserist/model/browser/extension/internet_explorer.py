from . import BrowserExtension
from .... import helper

class InternetExplorerBrowserExtension(BrowserExtension):
    def enable_images(self) -> None:
        """Intended use: Revert disabled images for Internet Explorer as its web driver doesn't support a session-based configuration for Selenium, but only a global configuration that impacts normal use."""

        helper.internet_explorer.enable_images(self.browser_driver)
