from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..wait.for_element import wait_for_element


def get_dimensions(browser_driver: BrowserDriver, xpath: str, timeout: float) -> tuple[int, int]:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    driver = browser_driver.get_webdriver()
    dimensions: dict[str, int] = driver.find_element(By.XPATH, xpath).size  # Returns dictionary object, e.g. {'height': 123, 'width': 456}.
    return dimensions.get("width") or 0, dimensions.get("height") or 0
