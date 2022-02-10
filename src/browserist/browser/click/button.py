from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ..wait.for_element import wait_for_element
from ...constant import timeout
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException

def click_button(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    wait_for_element(driver, xpath, timeout)
    try:
        button = driver.find_element_by_xpath(xpath)
        button.click()
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
