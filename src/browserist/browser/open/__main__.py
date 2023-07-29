from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .url import open_url
from .url_if_not_current import open_url_if_not_current


class OpenDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def url(self, url: str) -> None:
        """Open web page by URL.

        Args:
            url (str): URL to open, e.g. `"https://example.com"`.
        """

        if self._timeout_should_continue():
            open_url(self._browser_driver, url)

    def url_if_not_current(self, url: str, ignore_trailing_slash: bool = True, ignore_parameters: bool = False, ignore_https: bool = False) -> None:
        """Open a URL if it isn't already the current URL.

        Tip:
            Useful when doing multiple operations on a page where you don't want to reload the page, but either A) only if it isn't a specific URL or B) to ensure that a process is only used on a specific page.

        Args:
            url (str): URL to open if not current URL, e.g. `"https://example.com"`.
            ignore_trailing_slash (bool, optional): Ignore whether the URL is `"https://example.com"` or `"https://example.com/"`.
            ignore_parameters (bool, optional): Ignore parameters in the URL, e.g. `"https://example.com/list?page=1"`.
            ignore_https (bool, optional): Ignore whether the URL is `"http://example.com"` or `"https://example.com"`.
        """

        if self._timeout_should_continue():
            open_url_if_not_current(self._browser_driver, url, ignore_trailing_slash, ignore_parameters, ignore_https)
