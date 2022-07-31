from selenium.webdriver.common.by import By

from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element


def get_attribute_values(browser_driver: BrowserDriver, xpath: str, attribute: str, timeout: int) -> list[str]:
    xpath = XPath(xpath)
    driver = browser_driver.get_webdriver()
    wait_for_element(driver, browser_driver.settings, xpath, timeout)
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    return [element.get_attribute(attribute) for element in elements]  # type: ignore
