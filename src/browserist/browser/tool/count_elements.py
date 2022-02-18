from selenium.webdriver.common.by import By
from ..wait.for_element import wait_for_element
from ...constant import timeout

def tool_count_elements(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> int:
    wait_for_element(driver, xpath, timeout)
    elements = driver.find_element(By.XPATH, xpath)
    return len(elements)
