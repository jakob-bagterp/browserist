from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .check_if_element_contains_text import check_if_element_contains_text
from .wait_for_element import wait_for_element
from ..constant import timeout
from ..exception.element import NoElementFoundException, NoElementFoundWithTextConditionException
from ..exception.timeout import WaitForElementTimeoutException
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def click_button(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    wait_for_element(driver, xpath, timeout)
    try:
        button = driver.find_element_by_xpath(xpath)
        button.click()
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath)

def click_button_if_contains_text(driver: object, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> None:
    try:
        wait_for_element(driver, xpath, timeout)
        if check_if_element_contains_text(driver, xpath, regex, ignore_case, timeout):
            click_button(driver, xpath, timeout)
        else:
            raise NoElementFoundWithTextConditionException(driver, xpath, regex)
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath)

class ClickDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def button(self, xpath: str, timeout: int = timeout.DEFAULT) -> None:
        """Click button."""

        click_button(self._driver, xpath, timeout)

    def button_if_contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> None:

        click_button_if_contains_text(self._driver, xpath, regex, ignore_case, timeout)
