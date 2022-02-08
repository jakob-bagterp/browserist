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
    elements = browser.find_elements_by_xpath(xpath)
    return [element.text for element in elements]

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
