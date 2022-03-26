from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from ...constant import timeout
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def input_value(driver: object, xpath: str, value: str, timeout: int = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    try:
        input_field = driver.find_element(By.XPATH, xpath)  # type: ignore
        # Always clear input field before entering value:
        input_field.clear()
        input_field.send_keys(value)
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
