from selenium.webdriver.common.by import By

from ... import iteration_helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_text(browser_driver: BrowserDriver, xpath: str, timeout: int) -> str:
    def get_inner_text_of_element(browser_driver: BrowserDriver, xpath: str) -> str:
        return browser_driver.webdriver.find_element(By.XPATH, xpath).text  # type: ignore

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    return iteration_helper.retry.get_text(browser_driver, xpath, get_inner_text_of_element)
