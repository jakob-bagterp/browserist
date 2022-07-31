from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_is_enabled(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    driver = browser_driver.get_webdriver()
    try:
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return element.is_enabled()  # type: ignore
    except (NoSuchElementException, Exception):
        return False
