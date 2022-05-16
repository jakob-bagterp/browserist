from ...model.type.xpath import XPath
from .is_enabled import check_if_is_enabled


def check_if_is_disabled(driver: object, xpath: str) -> bool:
    xpath = XPath(xpath)
    return not check_if_is_enabled(driver, xpath)
