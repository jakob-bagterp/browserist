from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_elements(driver: object, xpath: str, timeout: int) -> list[object]:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    return driver.find_elements(By.XPATH, xpath)  # type: ignore
