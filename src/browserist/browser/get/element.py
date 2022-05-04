from selenium.webdriver.common.by import By

from ...constant import timeout
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> object:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    return driver.find_element(By.XPATH, xpath)  # type: ignore
