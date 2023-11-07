from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ...model.browser.base.driver import BrowserDriver
from ..wait.for_element import wait_for_element


def get_elements_by_tag(browser_driver: BrowserDriver, tag: str, timeout: float) -> list[WebElement]:
    wait_for_element(browser_driver, f"//{tag}", timeout)
    driver = browser_driver.get_webdriver()
    return driver.find_elements(By.TAG_NAME, tag)
