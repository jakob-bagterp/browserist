from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..wait.for_element import wait_for_element
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException

def input_clear(driver: object, xpath: str) -> None:
    wait_for_element(driver, xpath)
    try:
        input_field = driver.find_element_by_xpath(xpath)
        input_field.clear()
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
