import re

from ...constant import timeout
from ...model.type.xpath import XPath
from ..get.text import get_text


def check_if_contains_text(driver: object, xpath: str, regex: str, ignore_case: bool = True, timeout: int = timeout.DEFAULT) -> bool:
    xpath = XPath(xpath)
    current_text = get_text(driver, xpath, timeout)
    if ignore_case:
        match = re.search(regex, current_text, re.IGNORECASE)
    else:
        match = re.search(regex, current_text)
    return bool(match)
