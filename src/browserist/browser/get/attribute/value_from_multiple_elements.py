from typing import List
from ...wait.for_element import wait_for_element
from ....constant import timeout

def get_attribute_value_from_multiple_elements(driver: object, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> List[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements_by_xpath(xpath)
    return [element.get_attribute(attribute) for element in elements]
