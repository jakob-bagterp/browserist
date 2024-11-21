from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .contains_any_text import wait_until_element_contains_any_text
from .download_file.__main__ import WaitUntilDownloadFileDriverMethods
from .element_disappears import wait_until_element_disappears
from .images_have_loaded import wait_until_images_have_loaded
from .is_clickable import wait_until_element_is_clickable
from .number_of_window_handles_is import wait_until_number_of_window_handles_is
from .page_title.__main__ import WaitUntilPageTitleDriverMethods
from .text.__main__ import WaitUntilTextDriverMethods
from .url.__main__ import WaitUntilUrlDriverMethods


class WaitUntilDriverMethods(DriverMethods):
    __slots__ = ["download_file", "page_title", "text", "url"]

    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        self.download_file: WaitUntilDownloadFileDriverMethods = WaitUntilDownloadFileDriverMethods(browser_driver)
        self.page_title: WaitUntilPageTitleDriverMethods = WaitUntilPageTitleDriverMethods(browser_driver)
        self.text: WaitUntilTextDriverMethods = WaitUntilTextDriverMethods(browser_driver)
        self.url: WaitUntilUrlDriverMethods = WaitUntilUrlDriverMethods(browser_driver)

    def contains_any_text(self, xpath: str, timeout: float | None = None) -> None:
        """Wait until element contains any text, e.g. an element in a single-page application that loads later than first page paint.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.until.contains_any_text("//h1")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_element_contains_any_text(self._browser_driver, xpath, timeout)

    def element_disappears(self, xpath: str, timeout: float | None = None) -> None:
        """Wait until element doesn't exist.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element to disappear. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="7"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.input.value("//xpath/to/input", "test")
                browser.click.button("//xpath/to/button")
                browser.wait.until.element_disappears("//xpath/to/input")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_element_disappears(self._browser_driver, xpath, timeout)

    def images_have_loaded(self, xpath: str = "//img", timeout: float | None = None) -> None:
        """Wait until the image(s) on the page have loaded.

        Args:
            xpath (str): XPath of the element. Can target one or more images. If `None`, all `<img>` image elements are targeted.
            timeout (float | None, optional): In seconds. Timeout to wait for element(s) to be loaded. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            As images often load after first page paint and sometimes require extra time to download, it's useful know when a specific image or all images have loaded. By default, this method targets all image elements on a page:

            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.until.images_have_loaded()
            ```

            If you don't want to target all image elements, you can target, for instance, the first image element by specifying the XPath:

            ```python title="" linenums="5"
                browser.wait.until.images_have_loaded("//img[1]")
            ```

            Or target all image elements with a specific class:

            ```python title="" linenums="5"
                browser.wait.until.images_have_loaded("//img[contains(@class, 'some-class')]")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_images_have_loaded(self._browser_driver, xpath, timeout)

    def is_clickable(self, xpath: str, timeout: float | None = None) -> None:
        """Wait until element is clickable.

        Args:
            xpath (str): XPath of the element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.wait.until.is_clickable("//xpath/to/button")
                browser.click.button("//xpath/to/button")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_element_is_clickable(self._browser_driver, xpath, timeout)

    def number_of_window_handles_is(self, expected_handles: int, timeout: float | None = None) -> None:
        """Wait until number of window handles is.

        Note:
            Useful when working with multiple tabs or browser windows as they sometimes take time to load.

        Args:
            expected_handles (int): Expected number of window handles.
            timeout (float | None, optional): In seconds. Timeout to wait for operation. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.window.open.new_tab("https://google.com")
                browser.wait.until.number_of_window_handles_is(2)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_number_of_window_handles_is(self._browser_driver, expected_handles, timeout)
