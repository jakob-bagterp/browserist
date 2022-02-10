from typing import List
from .current_page_title import get_current_page_title
from .current_url import get_current_url
from .dimensions_of_element import get_dimensions_of_element
from .text_from_element import get_text_from_element
from .texts_from_multiple_elements import get_texts_from_multiple_elements
from .url_from_image import get_url_from_image
from .url_from_link import get_url_from_link
from .urls_from_multiple_images import get_urls_from_multiple_images
from .urls_from_multiple_links import get_urls_from_multiple_links
from .value_from_attribute import get_value_from_attribute
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods

class GetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        
    def current_page_title(self) -> str:
        """Get page title of the current page."""

        return get_current_page_title(self._driver)

    def current_url(self) -> str:
        """Get URL of the current page."""

        return get_current_url(self._driver)

    def dimensions_of_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> tuple[int, int]:
        """Get width and height of element in pixels. Usage:

        width, height = browser.get.dimensions_of_element("/element/xpath")"""

        return get_dimensions_of_element(self._driver, xpath, timeout)

    def text_from_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get text from element.

        This method assumes that the text field shouldn't be empty and therefore will retry to get the text (for better support of single-page apps with extended loading time)."""

        return get_text_from_element(self._driver, xpath, timeout)

    def texts_from_multiple_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
        """Get array of texts from elements.

        Assumes that the XPath targets multiple elements."""

        return get_texts_from_multiple_elements(self._driver, xpath, timeout)

    def url_from_image(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get URL source from image, e.g. <img> tag.

        This method assumes that the image shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        return get_url_from_image(self._driver, xpath, timeout)

    def urls_from_multiple_images(self, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
        """Get array of URLs from images, e.g. <img> tags.

        Assumes that the XPath targets multiple images."""

        return get_urls_from_multiple_images(self._driver, xpath, timeout)

    def url_from_link(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get URL from link, e.g. <a> tag or button.

        This method assumes that the link shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        return get_url_from_link(self._driver, xpath, timeout)

    def urls_from_multiple_links(self, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
        """Get array of URLs from links, e.g. <a> tags or buttons.

        Assumes that the XPath targets multiple links."""

        return get_urls_from_multiple_links(self._driver, xpath, timeout)

    def get_value_from_attribute(self, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> str:
        """Get value from an attribute of an element. Examples:

        Use "src" as attribute to get the source URL from an <img> image tag.

        Use "href" as attribute to get the URL from an <a> link tag."""

        return get_value_from_attribute(self._driver, xpath, attribute, timeout)
