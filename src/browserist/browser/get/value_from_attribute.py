from ..wait.for_element import wait_for_element
from ...constant import timeout

def get_value_from_attribute(driver: object, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> str:
    wait_for_element(driver, xpath, timeout)
    return driver.find_element_by_xpath(xpath).get_attribute(attribute)
