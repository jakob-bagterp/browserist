from .....model.browser.base.driver import BrowserDriver
from .....model.driver_methods import DriverMethods
from .changes import wait_until_url_changes
from .contains import wait_until_url_contains
from .equals import wait_until_url_equals


class WaitUntilUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def changes(self, baseline_url: str, timeout: float | None = None) -> None:
        """Wait until the browser URL has changed compared to a baseline URL, e.g. after a redirect or form action.

        Args:
            baseline_url (str): Baseline URL to compare the new URL to. It's evaluated as any change.
            timeout (float | None, optional): In seconds. Timeout to wait for URL to change. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="7"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                baseline_url = browser.get.url.current()
                browser.click.button("//xpath/to/button")
                browser.wait.until.url.changes(baseline_url)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_url_changes(self._browser_driver, baseline_url, timeout)

    def contains(self, url_fragment: str, timeout: float | None = None) -> None:
        """Wait until the browser URL contains a specified text fragment, e.g. after a redirect or updated query string.

        Args:
            url_fragment (str):  The URL variable can contain both a fragment (e.g. `"?login=true"`) or a full URL (e.g. `"https://example.com?login=true"`).
            timeout (float | None, optional): In seconds. Timeout to wait for URL to contain the specified fragment. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.click.button("//xpath/to/button")
                browser.wait.until.url.contains("some_page_name")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_url_contains(self._browser_driver, url_fragment, timeout)

    def equals(self, url: str, timeout: float | None = None) -> None:
        """Wait until the browser URL has changed to a specific URL, e.g. after a redirect or clicking a button.

        Args:
            url (str): Full URL to compare the new URL against. Evaluated as an exact match.
            timeout (float | None, optional): In seconds. Timeout to wait for URL to match the specified URL. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.click.button("//xpath/to/button")
                browser.wait.until.url.equals("https://example.com/some_page_name")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_url_equals(self._browser_driver, url, timeout)
