from pathlib import Path

from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .complete_page import get_screenshot_of_complete_page
from .element import get_screenshot_of_element
from .visible_portion import get_screenshot_of_visible_portion


class ScreenshotDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def complete_page(self, file_name: str | None = None, destination_dir: str | Path | None = None, delay_seconds: float = 0.25) -> None:
        """Take screenshot of the complete current page and save as PNG image.

        Note:
            Firefox is recommended browser for complete page screenshots as it executes this in one go. Other browsers can't capture the entire page at once, and so we need to merge screenshots portion by portions – and this is obviously much slower. For example:

            ```python title="" linenums="1" hl_lines="3 7"
            from browserist import Browser, BrowserSettings, BrowserType

            settings = BrowserSettings(browser_type=BrowserType.FIREFOX)

            with Browser(settings) as browser:
                browser.open.url("https://example.com")
                browser.screenshot.complete_page()
            ```

        Args:
            file_name (str | None, optional): Name of the file. If `None`, the file name is generated automatically.
            destination_dir (str | Path | None, optional): Destination directory. If `None`, the directory defined in the browser settings is used.
            delay_seconds (float, optional): As we stitch several screenshots together by scrolling down the page, adjust iteration delay to ensure that the screen is updated after each scroll.

        Example:
            Default file name and destination:

            ```python title=""
            browser.screenshot.complete_page()
            ```

            Custom file name and default destination:

            ```python title=""
            browser.screenshot.complete_page("image.png")
            ```

            Custom file name and destination:

            ```python title=""
            browser.screenshot.complete_page("image.png", "/screenshots/folder")
            ```

            Default file name and custom destination:

            ```python title=""
            browser.screenshot.complete_page(destination_dir="/screenshots/folder")
            ```

        Note:
            When setting a custom file name, screenshots should always be saved as a PNG file with a `.png` extension.
        """

        if self._timeout_should_continue():
            get_screenshot_of_complete_page(self._browser_driver, file_name, destination_dir, delay_seconds)

    def element(self, xpath: str, file_name: str | None = None, destination_dir: str | Path | None = None) -> None:
        """Take screenshot of an element on the current page and save as PNG image.

        Args:
            xpath (str): XPath of the element.
            file_name (str | None, optional): Name of the file. If `None`, the file name is generated automatically.
            destination_dir (str | Path | None, optional): Destination directory. If `None`, the directory defined in the browser settings is used.

        Example:
            Default file name and destination:

            ```python title=""
            browser.screenshot.element("//xpath/to/element")
            ```

            Custom file name and default destination:

            ```python title=""
            browser.screenshot.element("//xpath/to/element", "image.png")
            ```

            Custom file name and destination:

            ```python title=""
            browser.screenshot.element("//xpath/to/element", "image.png", "/screenshots/folder")
            ```

            Default file name and custom destination:

            ```python title=""
            browser.screenshot.element("//xpath/to/element", destination_dir="/screenshots/folder")
            ```

        Note:
            When setting a custom file name, screenshots should always be saved as a PNG file with a `.png` extension.
        """

        if self._timeout_should_continue():
            get_screenshot_of_element(self._browser_driver, xpath, file_name, destination_dir)

    def visible_portion(self, file_name: str | None = None, destination_dir: str | Path | None = None) -> None:
        """Take screenshot of the visible portion of the current page and save as PNG image.

        Args:
            file_name (str | None, optional): Name of the file. If `None`, the file name is generated automatically.
            destination_dir (str | Path | None, optional): Destination directory. If `None`, the directory defined in the browser settings is used.

        Example:
            Default file name and destination:

            ```python title=""
            browser.screenshot.visible_portion()
            ```

            Custom file name and default destination:

            ```python title=""
            browser.screenshot.visible_portion("image.png")
            ```

            Custom file name and destination:

            ```python title=""
            browser.screenshot.visible_portion("image.png", "/screenshots/folder")
            ```

            Default file name and custom destination:

            ```python title=""
            browser.screenshot.visible_portion(destination_dir="/screenshots/folder")
            ```

        Note:
            When setting a custom file name, screenshots should always be saved as a PNG file with a `.png` extension.
        """

        if self._timeout_should_continue():
            get_screenshot_of_visible_portion(self._browser_driver, file_name, destination_dir)
