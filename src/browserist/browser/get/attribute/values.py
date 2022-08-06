from selenium.webdriver.common.by import By

from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element


def get_attribute_values(browser_driver: BrowserDriver, xpath: str, attribute: str, timeout: float) -> list[str]:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    elements: list[object] = driver.find_elements(By.XPATH, xpath)  # type: ignore
    return [element.get_attribute(attribute) for element in elements]  # type: ignore
