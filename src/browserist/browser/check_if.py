from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .check_if_does_element_exist import check_if_does_element_exist
from .wait_for_element import wait_for_element
from ..constant import timeout
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

def check_if_is_element_clickable(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
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
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.is_enabled()
    except NoSuchElementException:
        return False

def check_if_is_element_disabled(driver: object, xpath: str) -> bool:
    return not check_if_is_element_enabled(driver, xpath)

def check_if_is_element_visible(driver: object, xpath: str) -> bool:
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.is_displayed()
    except NoSuchElementException:
        return False

def check_if_is_image_element_loaded(driver: object, element: object) -> bool:
    is_image_loaded = driver.execute_script(
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
        element)
    return is_image_loaded

def check_if_is_image_loaded(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
    wait_for_element(driver, xpath, timeout)
    element = driver.find_element_by_xpath(xpath)
    return check_if_is_image_element_loaded(driver, element)

class CheckIfDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def does_element_exist(self, xpath: str,) -> bool:
        """Check if element exists."""

        return check_if_does_element_exist(self._driver, xpath)

    def is_element_clickable(self, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
        """Check if element is clickable."""

        return check_if_is_element_clickable(self._driver, xpath, timeout)

    def is_element_enabled(self, xpath: str) -> bool:
        """Check whether element is enabled."""

        return check_if_is_element_enabled(self._driver, xpath)

    def is_element_disabled(self, xpath: str) -> bool:
        """Check whether element is disabled."""

        return check_if_is_element_disabled(self._driver, xpath)

    def is_element_visible(self, xpath: str) -> bool:
        """Check visibility status of an element."""

        return check_if_is_element_visible(self._driver, xpath)

    def is_image_loaded(self, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
        """Check is image is loaded and ready in the DOM."""

        return check_if_is_image_loaded(self._driver, xpath, timeout)

    def is_image_element_loaded(self, element: object) -> bool:
        """Check is image element is loaded and ready in the DOM."""

        return check_if_is_image_element_loaded(self._driver, element)
