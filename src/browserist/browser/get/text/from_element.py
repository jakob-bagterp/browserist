from selenium.webdriver.common.by import By

from .... import helper
from ....constant import timeout
from ...wait.for_element import wait_for_element


def get_text_from_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_inner_text_of_element(driver: object, xpath: str) -> str:
        return driver.find_element(By.XPATH, xpath).text

    wait_for_element(driver, xpath, timeout)
    return helper.retry.get_text_from_element(get_inner_text_of_element(driver, xpath))
