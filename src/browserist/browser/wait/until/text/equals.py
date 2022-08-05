import re

from ..... import constant, iteration_helper
from .....model.browser.base.driver import BrowserDriver
from .....model.type.xpath import XPath
from ....get.text import get_text
from ...for_element import wait_for_element


def wait_until_text_equals(browser_driver: BrowserDriver, xpath: str, regex: str, timeout: int) -> None:
    def is_element_text(browser_driver: BrowserDriver, xpath: str, regex: str) -> bool:
        text = get_text(browser_driver, xpath, constant.timeout.BYPASS)
        return bool(re.match(regex, text))

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    iteration_helper.retry.until_condition_is_true(
        browser_driver.webdriver, browser_driver.settings, xpath, regex, func=is_element_text, timeout=timeout)
