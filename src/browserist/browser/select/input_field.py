from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def select_input_field(browser_driver: BrowserDriver, xpath: str, timeout: int) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver.webdriver, browser_driver.settings, xpath, timeout)
    driver = browser_driver.get_webdriver()
    driver.find_element(By.XPATH, xpath).click()  # type: ignore
