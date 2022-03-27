from selenium.webdriver.common.by import By

from ....constant import timeout
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element


def get_text_from_multiple_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    return [element.text for element in elements]  # type: ignore
