import time
from typing import List
from .get_current_url import get_current_url
from .wait import wait_for_element
from ..constant import timeout
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def get_text_from_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_inner_text_of_element(xpath: str) -> str:
        return driver.find_element_by_xpath(xpath).text
    
    wait_for_element(driver, xpath, timeout)
    text = get_inner_text_of_element(xpath)
    i = 0
    while len(text) == 0 and i < 10:
        time.sleep(0.5)
        text = get_inner_text_of_element(xpath)
        i += 1
    return text

def get_texts_from_multiple_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return [element.text for element in elements]

def get_url_from_link(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_href_attribute_of_element(xpath: str) -> str:
        return driver.find_element_by_xpath(xpath).get_attribute("href")

    wait_for_element(driver, xpath, timeout)
    url = get_href_attribute_of_element(xpath)
    i = 0
    while len(url) == 0 and i < 10:
        time.sleep(0.5)
        url = get_href_attribute_of_element(xpath)
        i += 1
    return url

class GetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def current_url(self) -> str:
        """Get URL of the current page."""

        return get_current_url(self._driver)

    def text_from_element(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get text from element.
        
        This method assumes that the text field shouldn't be empty and therefore will retry to get the text (for better support of single-page apps with extended loading time)."""

        return get_text_from_element(self._driver, xpath, timeout)

    def texts_from_multiple_elements(self, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
        """Get array of texts from elements.
        
        Assumes that the XPath targets multiple elements."""
        
        return get_texts_from_multiple_elements(self._driver, xpath, timeout)

    def url_from_link(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get URL from link, e.g. <a> tag or button.

        This method assumes that the link shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        return get_url_from_link(self._driver, xpath, timeout)
