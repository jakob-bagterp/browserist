from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from ...constant import timeout
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException
from ..wait.for_element import wait_for_element


def input_value(driver: object, xpath: str, value: str, timeout: int = timeout.DEFAULT) -> None:
    wait_for_element(driver, xpath, timeout)
    try:
        input_field = driver.find_element(By.XPATH, xpath)
        input_field.clear()  # Always clear input field before entering value
        input_field.send_keys(value)
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
