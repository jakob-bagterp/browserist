from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def input_clear(browser_driver: BrowserDriver, xpath: str, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver.webdriver, browser_driver.settings, xpath, timeout)
    driver = browser_driver.get_webdriver()
    input_field_element = driver.find_element(By.XPATH, xpath)  # type: ignore
    input_field_element.clear()
