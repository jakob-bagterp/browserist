from selenium.webdriver.common.by import By

from ...constant import timeout
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element
from .is_image_element_loaded import check_if_is_image_element_loaded


def check_if_is_image_loaded(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    element: object = driver.find_element(By.XPATH, xpath)  # type: ignore
    return check_if_is_image_element_loaded(driver, element)
