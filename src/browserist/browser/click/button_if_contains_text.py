from selenium.common.exceptions import NoSuchElementException, TimeoutException

from ...constant import timeout
from ...exception.element import NoElementFoundException, NoElementFoundWithTextConditionException
from ...exception.timeout import WaitForElementTimeoutException
from ...model.type.xpath import XPath
from ..check_if.element_contains_text import check_if_element_contains_text
from ..wait.for_element import wait_for_element
from .button import click_button


def click_button_if_contains_text(driver: object, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    try:
        wait_for_element(driver, xpath, timeout)
        if check_if_element_contains_text(driver, xpath, regex, ignore_case, timeout):
            click_button(driver, xpath, timeout)
        else:
            raise NoElementFoundWithTextConditionException(driver, xpath, regex)
    except TimeoutException:
        raise WaitForElementTimeoutException(driver, xpath) from TimeoutException
    except NoSuchElementException:
        raise NoElementFoundException(driver, xpath) from NoSuchElementException
