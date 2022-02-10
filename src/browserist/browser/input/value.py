from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..wait.for_element import wait_for_element
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException

def input_value(driver: object, xpath: str, value: str) -> None:
    wait_for_element(driver, xpath)
    try:
        input_field = driver.find_element_by_xpath(xpath)
        input_field.clear() # Always clear input field before entering value
        input_field.send_keys(value)
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
