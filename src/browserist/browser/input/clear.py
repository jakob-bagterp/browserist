from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..wait.for_element import wait_for_element
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException

def input_clear(driver: object, input_xpath: str) -> None:
    wait_for_element(driver, input_xpath)
    try:
        input_field = driver.find_element_by_xpath(input_xpath)
        input_field.clear()
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, input_xpath)
    except NoSuchElementException:
        raise NoElementFoundException(driver, input_xpath)
