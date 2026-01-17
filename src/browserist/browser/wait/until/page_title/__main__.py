from .....model.browser.base.driver import BrowserDriver
from .....model.driver_methods import DriverMethods
from .changes import wait_until_page_title_changes
from .contains import wait_until_page_title_contains
from .equals import wait_until_page_title_equals


class WaitUntilPageTitleDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def changes(self, baseline_text: str, timeout: float | None = None) -> None:
        """Wait until the page title of the current page changes compared to a baseline text, e.g. after a page reload or update.

        Args:
            baseline_text (str): Baseline text to compare current page title against. It's evaluated as any change.
            timeout (float | None, optional): In seconds. Timeout to wait for page title to change. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="7"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                baseline_text = browser.get.page_title()
                browser.click.button("//xpath/to/button")
                browser.wait.until.page_title.changes(baseline_text)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_page_title_changes(self._browser_driver, baseline_text, timeout)

    def contains(self, page_title_fragment: str, timeout: float | None = None) -> None:
        """Wait until the page title of the current page contains a specified text fragment, e.g. after a redirect or update.

        Args:
            page_title_fragment (str): The input can contain both a fragment or the full page title.
            timeout (float | None, optional): In seconds. Timeout to wait for page title to contain text fragment. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.until.page_title.contains("Example")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_page_title_contains(self._browser_driver, page_title_fragment, timeout)

    def equals(self, page_title: str, timeout: float | None = None) -> None:
        """Wait until the page title of the current page has changed to a specific text, e.g. after a redirect or update.

        Args:
            page_title (str): Full page title to compare the new current page title against. Evaluated as an exact match.
            timeout (float | None, optional): In seconds. Timeout to wait for page title to match specified text. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.until.page_title.equals("Example Domain")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_page_title_equals(self._browser_driver, page_title, timeout)
