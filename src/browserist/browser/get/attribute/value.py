from selenium.webdriver.common.by import By

from ....model.browser.base.settings import BrowserSettings
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element


def get_attribute_value(driver: object, settings: BrowserSettings, xpath: str, attribute: str, timeout: int) -> str:
    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    return driver.find_element(By.XPATH, xpath).get_attribute(attribute)  # type: ignore
