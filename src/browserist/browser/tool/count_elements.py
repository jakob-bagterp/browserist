from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def tool_count_elements(browser_driver: BrowserDriver, xpath: str, timeout: float) -> int:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    return len(elements)
