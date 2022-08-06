from selenium.webdriver.common.by import By

from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def check_if_is_image_loaded(browser_driver: BrowserDriver, xpath: str, timeout: float) -> bool:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    element: object = driver.find_element(By.XPATH, xpath)  # type: ignore
    return helper.image.is_element_loaded(driver, element)
