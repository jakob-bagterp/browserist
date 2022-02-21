from .... import factory
from .__main__ import BrowserExtension


class InternetExplorerBrowserExtension(BrowserExtension):
    def enable_images(self) -> None:
        """Intended use: Revert disabled images for Internet Explorer as its web driver doesn't support a session-based configuration for Selenium, but only a global configuration that impacts normal use."""

        factory.internet_explorer.enable_images(self.browser_driver)
