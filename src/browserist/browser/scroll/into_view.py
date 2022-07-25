import time

from selenium.webdriver.common.by import By

from ...model.browser.base.settings import BrowserSettings
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def scroll_into_view(driver: object, settings: BrowserSettings, xpath: str, timeout: int, delay_seconds: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    element: object = driver.find_element(By.XPATH, xpath)  # type: ignore
    driver.execute_script("arguments[0].scrollIntoView();", element)  # type: ignore
    time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
