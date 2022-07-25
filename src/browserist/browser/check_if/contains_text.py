import re

from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..get.text import get_text


def check_if_contains_text(driver: object, settings: BrowserSettings, xpath: str, regex: str, ignore_case: bool, timeout: int) -> bool:
    xpath = XPath(xpath)
    current_text = get_text(driver, settings, xpath, timeout)
    if ignore_case:
        match = re.search(regex, current_text, re.IGNORECASE)
    else:
        match = re.search(regex, current_text)
    return bool(match)
