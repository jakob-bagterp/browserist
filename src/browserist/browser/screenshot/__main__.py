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
        """Take screenshot of complete page and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.screenshot.complete_page() # Default file name and destination

        browser.screenshot.complete_page("image.png") # Custom file name and default destination

        browser.screenshot.complete_page("image.png", "./screenshots") # Custom file name and destination

        browser.screenshot.complete_page(destination_dir = "./screenshots") # Default file name and custom destination

        Firefox is recommended browser for complete page screenshots as it executes this in one go. Other browsers can't capture the entire page at once, and so we need to merge screenshots portion by portions – this is obviously much slower.

        Use "delay_seconds" to adjust iteration delay to ensure that the screen is updated after each scroll."""

        if self._timeout_should_continue():
            get_screenshot_of_complete_page(self._browser_driver, file_name, destination_dir, delay_seconds)

    def element(self, xpath: str, file_name: str | None = None, destination_dir: str | Path | None = None) -> None:
        """Take screenshot of visible portion and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.screenshot.element("/element/xpath") # Default file name and destination

        browser.screenshot.element("/element/xpath", "image.png") # Custom file name and default destination

        browser.screenshot.element("/element/xpath", "image.png", "./screenshots") # Custom file name and destination

        browser.screenshot.element("/element/xpath", destination_dir = "./screenshots") # Default file name and custom destination

        Note that "/element/xpath" should be a valid XPath expression."""

        if self._timeout_should_continue():
            get_screenshot_of_element(self._browser_driver, xpath, file_name, destination_dir)

    def visible_portion(self, file_name: str | None = None, destination_dir: str | Path | None = None) -> None:
        """Take screenshot of visible portion and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.screenshot.visible_portion() # Default file name and destination

        browser.screenshot.visible_portion("image.png") # Custom file name and default destination

        browser.screenshot.visible_portion("image.png", "./screenshots") # Custom file name and destination

        browser.screenshot.visible_portion(destination_dir = "./screenshots") # Default file name and custom destination"""

        if self._timeout_should_continue():
            get_screenshot_of_visible_portion(self._browser_driver, file_name, destination_dir)
