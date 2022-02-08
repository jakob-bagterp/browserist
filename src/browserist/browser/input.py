from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .wait_for_element import wait_for_element
from ..exception.element import NoElementFoundException
from ..exception.timeout import WaitForElementTimeoutException
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def input_clear(driver: object, input_xpath: str) -> None:
    wait_for_element(driver, input_xpath)
    try:
        input_field = driver.find_element_by_xpath(input_xpath)
        input_field.clear()
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, input_xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, input_xpath)

def input_value(driver: object, input_xpath: str, value: str) -> None:
    wait_for_element(driver, input_xpath)
    try:
        input_field = driver.find_element_by_xpath(input_xpath)
        input_field.clear() # Always clear input field before entering value
        input_field.send_keys(value)
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, input_xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, input_xpath)

class InputDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
    
    def clear(self, input_xpath: str) -> None:
        """Clear input form field."""

        input_clear(self._driver, input_xpath)

    def value(self, input_xpath: str, value: str) -> None:
        """Input value into form field."""

        input_value(self._driver, input_xpath, value)
