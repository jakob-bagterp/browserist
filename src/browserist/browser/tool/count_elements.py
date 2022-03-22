from selenium.webdriver.common.by import By

from ...constant import timeout
from ..wait.for_element import wait_for_element


def tool_count_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> int:
    wait_for_element(driver, xpath, timeout)
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    return len(elements)
