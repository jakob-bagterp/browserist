import re

from ..... import constant, helper_iteration
from .....model.browser.base.driver import BrowserDriver
from .....model.type.xpath import XPath
from ....get.text import get_text
from ...for_element import wait_for_element


def wait_until_text_equals(browser_driver: BrowserDriver, xpath: str, regex: str, timeout: float) -> None:
    def is_element_text(browser_driver: BrowserDriver, xpath: str, regex: str) -> bool:
        text = get_text(browser_driver, xpath, constant.timeout.BYPASS)
        return bool(re.match(regex, text))

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    helper_iteration.retry.until_condition_is_true(browser_driver, xpath, regex, func=is_element_text, timeout=timeout)
