import re

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait


def check_if_contains_text(browser_driver: BrowserDriver, xpath: str, regex: str, ignore_case: bool = True) -> bool:
    xpath = XPath(xpath)
    try:
        element = get_element_without_wait(browser_driver, xpath)
        text = str(element.text)
        match = re.search(regex, text, re.IGNORECASE) if ignore_case else re.search(regex, text)
        return bool(match)
    except Exception:
        return False
