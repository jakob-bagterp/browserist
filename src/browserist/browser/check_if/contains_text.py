import re

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.text import get_text


def check_if_contains_text(browser_driver: BrowserDriver, xpath: str, regex: str, ignore_case: bool, timeout: float) -> bool:
    xpath = XPath(xpath)
    current_text = get_text(browser_driver, xpath, timeout)
    if ignore_case:
        match = re.search(regex, current_text, re.IGNORECASE)
    else:
        match = re.search(regex, current_text)
    return bool(match)
