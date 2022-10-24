from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_elements(browser_driver: BrowserDriver, xpath: str, timeout: float) -> list[object]:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    return get_elements_without_wait(browser_driver, xpath)


def get_elements_without_wait(browser_driver: BrowserDriver, xpath: XPath) -> list[object]:
    """Variation of the get_elements() method for internal use only. It assumes that the XPath has already been validated."""

    driver = browser_driver.get_webdriver()
    return driver.find_elements(By.XPATH, xpath)  # type: ignore
