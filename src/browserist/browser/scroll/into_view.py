import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from ... import constant
from ...constant import timeout
from ...exception.element import NoElementFoundException
from ...exception.timeout import WaitForElementTimeoutException
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def scroll_into_view(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    try:
        wait_for_element(driver, xpath, timeout)
        element: object = driver.find_element(By.XPATH, xpath)  # type: ignore
        driver.execute_script("arguments[0].scrollIntoView();", element)  # type: ignore
        time.sleep(constant.timeout.SHORT)  # Small timeout to make sure screen is updated after scroll.
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
