import time

from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..tool.execute_script import execute_script
from ..wait.for_element import wait_for_element


def scroll_into_view(browser_driver: BrowserDriver, xpath: str, timeout: float, delay_seconds: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    element = driver.find_element(By.XPATH, xpath)  # type: ignore
    execute_script(browser_driver, "arguments[0].scrollIntoView();", element)
    time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
