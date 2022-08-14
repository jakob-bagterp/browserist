from ... import constant
from ...exception.element import NoElementFoundWithTextConditionException
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..check_if.contains_text import check_if_contains_text
from ..wait.for_element import wait_for_element
from .button import click_button


def click_button_if_contains_text(browser_driver: BrowserDriver, xpath: str, regex: str, ignore_case: bool, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    if check_if_contains_text(browser_driver, xpath, regex, ignore_case):
        # We bypass the timeout since we know the element is present following the wait_for_element() check:
        click_button(browser_driver, xpath, constant.timeout.BYPASS)
    else:
        raise NoElementFoundWithTextConditionException(browser_driver, xpath, regex)
