from typing import List
from ..attribute.value_from_multiple_elements import get_attribute_value_from_multiple_elements
from ....constant import timeout

def get_url_from_multiple_images(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> List[str]:
    return get_attribute_value_from_multiple_elements(driver, xpath, "src", timeout)
