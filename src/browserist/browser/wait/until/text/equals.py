import re

from ..... import constant, helper
from .....model.browser.base.settings import BrowserSettings
from .....model.type.xpath import XPath
from ....get.text import get_text
from ...for_element import wait_for_element


def wait_until_text_equals(driver: object, settings: BrowserSettings, xpath: str, regex: str, timeout: int) -> None:
    def is_element_text(driver: object, settings: BrowserSettings, xpath: str, regex: str) -> bool:
        text = get_text(driver, settings, xpath, constant.timeout.BYPASS)
        return bool(re.match(regex, text))

    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    helper.retry.until_condition_is_true(driver, settings, xpath, regex, func=is_element_text, timeout=timeout)
