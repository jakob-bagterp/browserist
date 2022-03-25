from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from ...model.type.xpath import XPath


def check_if_does_element_exist(driver: object, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        element: object = driver.find_element(By.XPATH, xpath)  # type: ignore
        return element is not None
    except (NoSuchElementException, Exception):
        return False
