from selenium.webdriver.common.by import By

from ...constant import timeout
from ..wait.for_element import wait_for_element


def get_all_elements_by_tag(driver: object, tag: str, timeout: int = timeout.DEFAULT) -> list[object]:
    wait_for_element(driver, f"//{tag}", timeout)
    return driver.find_elements(By.TAG_NAME, tag)
