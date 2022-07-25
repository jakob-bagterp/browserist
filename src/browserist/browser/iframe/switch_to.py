from selenium.webdriver.common.by import By

from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def switch_to_iframe(driver: object, settings: BrowserSettings, xpath: str, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    iframe_element = driver.find_element(By.XPATH, xpath)  # type: ignore
    driver.switch_to.frame(iframe_element)  # type: ignore
