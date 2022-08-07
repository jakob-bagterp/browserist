from selenium.webdriver.common.by import By

from ... import helper
from ...model.type.xpath import XPath


def check_if_is_image_loaded(driver: object, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return helper.image.is_element_loaded(driver, element)
    except Exception:
        return False
