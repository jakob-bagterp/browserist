import time
from .wait import wait_for_element
from ..constant import timeout
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def get_current_url(driver: object) -> str:
    return driver.current_url

def get_text(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
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

class GetDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def current_url(self) -> str:
        """Get URL of the current page."""
        
        return get_current_url(self._driver)

    def text(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get text from element.
        
        This method assumes that the text field shouldn't be empty and therefore will retry to get the text (for better support of single-page apps with extended loading time)."""

        return get_text(self._driver, xpath, timeout)
