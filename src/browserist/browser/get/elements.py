from selenium.webdriver.common.by import By

from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_elements(driver: object, settings: BrowserSettings, xpath: str, timeout: int) -> list[object]:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    return driver.find_elements(By.XPATH, xpath)  # type: ignore
