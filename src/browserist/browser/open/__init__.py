from .url import open_url
from .url_if_not_current import open_url_if_not_current
from .url_in_new_tab import open_url_in_new_tab
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

class OpenDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def url(self, url: str) -> None:
        """Open web page by URL."""
        
        open_url(self._driver, url)

    def url_if_not_current(self, url: str, ignore_trailing_slash: bool = True) -> None:
        """Open a URL if it isn't already the current URL. Useful when doing multiple operations on a page where."""

        open_url_if_not_current(self._driver, url, ignore_trailing_slash)

    def url_in_new_tab(self, url: str) -> None:
        """Open a link in a new browser tab with support across browsers."""

        open_url_in_new_tab(self._driver, url)
