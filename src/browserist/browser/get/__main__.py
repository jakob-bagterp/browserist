from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.driver_methods import DriverMethods
from .all_elements_by_tag import get_all_elements_by_tag
from .attribute.__main__ import GetAttributeDriverMethods
from .dimensions_of_element import get_dimensions_of_element
from .page_title import get_page_title
from .screenshot import get_screenshot
from .text.__main__ import GetTextDriverMethods
from .url.__main__ import GetUrlDriverMethods


class GetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)
        self.attribute: GetAttributeDriverMethods = GetAttributeDriverMethods(browser_driver, settings)
        self.text: GetTextDriverMethods = GetTextDriverMethods(browser_driver, settings)
        self.url: GetUrlDriverMethods = GetUrlDriverMethods(browser_driver, settings)

    def all_elements_by_tag(self, tag: str, timeout: int = timeout.DEFAULT) -> list[object]:
        """"Get all elements by HTML tag. Examples: "img" as tag for all <img> images, "a" for all <a> links, etc."""

        return get_all_elements_by_tag(self._driver, tag, timeout)

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

        browser.get.screenshot("image.png") # Custom file name and default destination

        browser.get.screenshot("image.png", "./screenshots") # Custom file name and destination

        browser.get.screenshot(destination_dir = "./screenshots") # Default file name and custom destination"""

        get_screenshot(self._driver, self._settings, file_name, destination_dir)
