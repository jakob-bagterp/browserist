from selenium.webdriver.common.by import By

from ... import helper
from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def check_if_is_image_loaded(driver: object, settings: BrowserSettings, xpath: str, timeout: int) -> bool:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    element: object = driver.find_element(By.XPATH, xpath)  # type: ignore
    return helper.image.is_element_loaded(driver, element)
