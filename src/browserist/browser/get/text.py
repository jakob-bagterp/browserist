from selenium.webdriver.common.by import By

from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_text(browser_driver: BrowserDriver, xpath: str, timeout: int) -> str:
    def get_inner_text_of_element(driver: object, _: BrowserSettings, xpath: str) -> str:
        return driver.find_element(By.XPATH, xpath).text  # type: ignore

    xpath = XPath(xpath)
    wait_for_element(browser_driver.webdriver, browser_driver.settings, xpath, timeout)
    return helper.retry.get_text(browser_driver.webdriver, browser_driver.settings, xpath, get_inner_text_of_element)
