from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def input_value(driver: object, xpath: str, value: str, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    input_field = driver.find_element(By.XPATH, xpath)  # type: ignore
    # Always clear input field before entering value:
    input_field.clear()
    input_field.send_keys(value)
