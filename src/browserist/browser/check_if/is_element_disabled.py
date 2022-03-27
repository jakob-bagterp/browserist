from ...model.type.xpath import XPath
from .is_element_enabled import check_if_is_element_enabled


def check_if_is_element_disabled(driver: object, xpath: str) -> bool:
    xpath = XPath(xpath)
    return not check_if_is_element_enabled(driver, xpath)
