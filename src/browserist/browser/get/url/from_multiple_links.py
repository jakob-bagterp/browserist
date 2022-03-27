from ....constant import timeout
from ....model.type.xpath import XPath
from ..attribute.value_from_multiple_elements import get_attribute_value_from_multiple_elements


def get_url_from_multiple_links(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
    xpath = XPath(xpath)
    return get_attribute_value_from_multiple_elements(driver, xpath, "href", timeout)
