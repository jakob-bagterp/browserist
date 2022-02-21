from selenium.webdriver.common.by import By

from ... import helper
from ...constant import timeout
from ..check_if.is_image_element_loaded import check_if_is_image_element_loaded
from .for_element import wait_for_element


def wait_until_images_have_loaded(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    def are_all_images_loaded(driver: object, elements: list[object]):
        return all(check_if_is_image_element_loaded(driver, element) is not False for element in elements)

    wait_for_element(driver, xpath, timeout)
    elements = driver.find_elements(By.XPATH, xpath)
    helper.retry.until_condition_is_true(are_all_images_loaded(driver, elements), timeout)
