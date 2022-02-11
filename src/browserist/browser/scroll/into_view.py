import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..wait.for_element import wait_for_element
from ... import constant
from ...constant import timeout
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException

def scroll_into_view(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    try:
        wait_for_element(driver, xpath, timeout)
        element = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(constant.timeout.SHORT) # Small timeout to make sure screen is updated after scroll.
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
