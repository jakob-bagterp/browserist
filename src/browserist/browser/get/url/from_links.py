from ....constant import timeout
from ....model.type.xpath import XPath
from ..attribute.values import get_attribute_values


def get_url_from_links(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
    xpath = XPath(xpath)
    return get_attribute_values(driver, xpath, "href", timeout)
