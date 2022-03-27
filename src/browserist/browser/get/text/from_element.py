from selenium.webdriver.common.by import By

from .... import helper
from ....constant import timeout
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element


def get_text_from_element(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_inner_text_of_element(driver: object, xpath: str) -> str:
        return driver.find_element(By.XPATH, xpath).text  # type: ignore

    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    return helper.retry.get_text_from_element(driver, xpath, get_inner_text_of_element)
