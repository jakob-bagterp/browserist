from typing import List
from .attribute import GetAttributeDriverMethods
from .dimensions_of_element import get_dimensions_of_element
from .page_title import get_page_title
from .screenshot import get_screenshot
from .text import GetTextDriverMethods
from .url import GetUrlDriverMethods
from .url_from_link import get_url_from_link
from .urls_from_multiple_images import get_urls_from_multiple_images
from .urls_from_multiple_links import get_urls_from_multiple_links
from .window_size import get_window_size
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods

class GetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.attribute: GetAttributeDriverMethods = GetAttributeDriverMethods(browser_driver, settings)
        self.text: GetTextDriverMethods = GetTextDriverMethods(browser_driver, settings)
        self.url: GetUrlDriverMethods = GetUrlDriverMethods(browser_driver, settings)

    def dimensions_of_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> tuple[int, int]:
        """Get width and height of element in pixels. Usage:

        width, height = browser.get.dimensions_of_element("/element/xpath")"""

        return get_dimensions_of_element(self._driver, xpath, timeout)

    def page_title(self) -> str:
        """Get page title of the current page."""

        return get_page_title(self._driver)

    def screenshot(self, file_name: str | None = None, destination_dir: str | None = None) -> None:
        """Take screenshot and save as PNG image. Default destination directory is from where the script is executed. Examples:

        browser.get.screenshot() # Default file name and destination

        browser.get.screenshot("image.png") # Custom file name and defualt destination

        browser.get.screenshot("image.png", "./screenshots") # Custom file name and destination

        browser.get.screenshot(destination_dir = "./screenshots") # Default file name and custom destination"""

        get_screenshot(self._driver, self._settings, file_name, destination_dir)

    def urls_from_multiple_images(self, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
        """Get array of URLs from images, e.g. <img> tags. Assumes that the XPath targets multiple images."""

        return get_urls_from_multiple_images(self._driver, xpath, timeout)

    def url_from_link(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get URL from link, e.g. <a> tag or button.

        This method assumes that the link shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        return get_url_from_link(self._driver, xpath, timeout)

    def urls_from_multiple_links(self, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
        """Get array of URLs from links, e.g. <a> tags or buttons. Assumes that the XPath targets multiple links."""

        return get_urls_from_multiple_links(self._driver, xpath, timeout)

    def window_size(self) -> tuple[int, int]:
        """Get width and height browser window in pixels. Usage:

        width, height = browser.get.window_size()"""

        return get_window_size(self._driver)
