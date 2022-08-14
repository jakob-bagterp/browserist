from selenium.webdriver.common.by import By

from ... import helper_iteration
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_text(browser_driver: BrowserDriver, xpath: str, timeout: float) -> str:
    def get_inner_text_of_element(browser_driver: BrowserDriver, xpath: str) -> str:
        driver = browser_driver.get_webdriver()
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return str(element.text)

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    return helper_iteration.retry.get_text(browser_driver, xpath, get_inner_text_of_element)
