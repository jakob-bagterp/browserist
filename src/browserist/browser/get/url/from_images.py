from ....model.type.xpath import XPath
from ..attribute.values import get_attribute_values


def get_url_from_images(driver: object, xpath: str, timeout: int) -> list[str]:
    xpath = XPath(xpath)
    return get_attribute_values(driver, xpath, "src", timeout)
