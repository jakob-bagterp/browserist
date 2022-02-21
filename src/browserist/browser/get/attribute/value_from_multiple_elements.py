from selenium.webdriver.common.by import By

from ....constant import timeout
from ...wait.for_element import wait_for_element


def get_attribute_value_from_multiple_elements(driver: object, xpath: str, attribute: str, timeout: int = timeout.DEFAULT) -> list[str]:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements(By.XPATH, xpath)
    return [element.get_attribute(attribute) for element in elements]
