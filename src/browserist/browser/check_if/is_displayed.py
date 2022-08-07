from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_is_displayed(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        driver = browser_driver.get_webdriver()
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return element.is_displayed()  # type: ignore
    except Exception:
        return False
