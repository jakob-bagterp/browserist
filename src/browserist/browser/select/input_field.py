from selenium.webdriver.common.by import By

from ...constant import timeout
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def select_input_field(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    driver.find_element(By.XPATH, xpath).click()  # type: ignore
