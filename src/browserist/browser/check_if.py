from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .wait import wait_for_element
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def check_if_is_element_clickable(driver: object, xpath: str, timeout: int = 5) -> bool:
    wait_for_element(driver, xpath, timeout)
    try:
        element = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element is not None
    except TimeoutException:
        return False
    except NoSuchElementException:
        return False

def check_if_is_element_enabled(driver: object, xpath: str) -> bool:
    wait_for_element(driver, xpath)
    element = driver.find_element_by_xpath(xpath)
    return element.is_enabled()

def check_if_is_element_disabled(driver: object, xpath: str) -> bool:
    return not check_if_is_element_enabled(driver, xpath)

class CheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def is_element_clickable(self, xpath: str, timeout: int = 5) -> bool:
        """Check if element by XPath is clickable."""
        
        return check_if_is_element_clickable(self._driver, xpath, timeout)

    def is_element_enabled(self, xpath: str) -> bool:
        """Check whether element is enabled."""

        return check_if_is_element_enabled(self._driver, xpath)

    def is_element_disabled(self, xpath: str) -> bool:
        """Check whether element is disabled."""

        return check_if_is_element_disabled(self._driver, xpath)
