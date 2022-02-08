from typing import List
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .get_current_page_title import get_current_page_title
from .get_current_url import get_current_url
from .wait_for_element import wait_for_element
from .. import helper
from ..constant import timeout
from ..exception.element import NoElementDimensionsFoundException
from ..exception.timeout import WaitForElementTimeoutException
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def get_dimensions_of_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> tuple[int, int]:
    wait_for_element(driver, xpath, timeout)
    try:
        dimensions = driver.find_element_by_xpath(xpath).size # Returns dictionary object, e.g. {'height': 598, 'width': 479}.
        return dimensions.get("width"), dimensions.get("height")
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath)
    except NoSuchElementException:
        raise NoElementDimensionsFoundException(driver, xpath)

def get_text_from_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_inner_text_of_element(driver: object, xpath: str) -> str:
        return driver.find_element_by_xpath(xpath).text

    wait_for_element(driver, xpath, timeout)
    return helper.driver.retry_and_get_text_from_element(get_inner_text_of_element(driver, xpath))

def get_texts_from_multiple_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return [element.text for element in elements]

def get_url_from_image(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_src_attribute_of_element(driver: object, xpath: str) -> str:
        return driver.find_element_by_xpath(xpath).get_attribute("src")

    wait_for_element(driver, xpath, timeout)
    return helper.driver.retry_and_get_text_from_element(get_src_attribute_of_element(driver, xpath))

def get_urls_from_multiple_images(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return [element.get_attribute("src") for element in elements]

def get_url_from_link(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_href_attribute_of_element(driver: object, xpath: str) -> str:
        return driver.find_element_by_xpath(xpath).get_attribute("href")

    wait_for_element(driver, xpath, timeout)
    return helper.driver.retry_and_get_text_from_element(get_href_attribute_of_element(driver, xpath))

def get_urls_from_multiple_links(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return [element.get_attribute("href") for element in elements]

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
