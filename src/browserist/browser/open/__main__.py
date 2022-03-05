from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .new_tab import open_new_tab
from .new_window import open_new_window
from .url import open_url
from .url_if_not_current import open_url_if_not_current


class OpenDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def new_tab(self, url: str | None = None) -> None:
        """Open and switch to new tab. The URL argument is optional."""

        open_new_tab(self._driver, url)

    def new_window(self, url: str | None = None) -> None:
        """Open and switch to new window. The URL argument is optional."""

        open_new_window(self._driver, url)

    def url(self, url: str) -> None:
        """Open web page by URL."""

        open_url(self._driver, url)

    def url_if_not_current(self, url: str, ignore_trailing_slash: bool = True, ignore_parameters: bool = False, ignore_https: bool = False) -> None:
        """Open a URL if it isn't already the current URL. Useful when doing multiple operations on a page where.

        ignore_trailing_slash: Ignore whether the URL is "http://example.com" or "http://example.com/".

        ignore_parameters: Ignore parameters in the URL, e.g. "http://example.com/list?page=1".

        ignore_https: Ignore whether the URL is "http://example.com" or "https://example.com"."""

        open_url_if_not_current(self._driver, url, ignore_trailing_slash, ignore_parameters, ignore_https)
