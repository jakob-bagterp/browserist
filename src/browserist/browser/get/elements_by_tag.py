from selenium.webdriver.common.by import By

from ...model.browser.base.settings import BrowserSettings
from ..wait.for_element import wait_for_element


def get_elements_by_tag(driver: object, settings: BrowserSettings, tag: str, timeout: int) -> list[object]:
    wait_for_element(driver, settings, f"//{tag}", timeout)
    return driver.find_elements(By.TAG_NAME, tag)  # type: ignore
