from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def input_value(browser_driver: BrowserDriver, xpath: str, value: str, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    input_field = driver.find_element(By.XPATH, xpath)
    # Always clear input field before entering value:
    input_field.clear()
    input_field.send_keys(value)
