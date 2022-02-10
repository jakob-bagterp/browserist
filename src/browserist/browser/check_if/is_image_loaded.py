from .is_image_element_loaded import check_if_is_image_element_loaded
from ..wait.for_element import wait_for_element
from ...constant import timeout

def check_if_is_image_loaded(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> bool:
    wait_for_element(driver, xpath, timeout)
    element = driver.find_element_by_xpath(xpath)
    return check_if_is_image_element_loaded(driver, element)
