from ....constant import timeout
from ..attribute.value_from_multiple_elements import get_attribute_value_from_multiple_elements


def get_url_from_multiple_links(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
    return get_attribute_value_from_multiple_elements(driver, xpath, "href", timeout)
