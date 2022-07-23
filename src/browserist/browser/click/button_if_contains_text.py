from ...exception.element import NoElementFoundWithTextConditionException
from ...model.type.xpath import XPath
from ..check_if.contains_text import check_if_contains_text
from ..wait.for_element import wait_for_element
from .button import click_button


def click_button_if_contains_text(driver: object, xpath: str, regex: str, ignore_case: bool, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    if check_if_contains_text(driver, xpath, regex, ignore_case, timeout):
        click_button(driver, xpath, timeout)
    else:
        raise NoElementFoundWithTextConditionException(driver, xpath, regex)
