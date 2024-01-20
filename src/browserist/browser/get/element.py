from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_element(browser_driver: BrowserDriver, xpath: str, timeout: float) -> WebElement:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    return get_element_without_wait(browser_driver, xpath)


def get_element_without_wait(browser_driver: BrowserDriver, xpath: XPath) -> WebElement:
    """Variation of the get_element() method for internal use only. It assumes that the XPath has already been validated."""

    driver = browser_driver.get_webdriver()
    return driver.find_element(By.XPATH, xpath)
