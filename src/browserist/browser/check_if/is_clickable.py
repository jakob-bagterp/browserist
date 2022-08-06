from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_is_clickable(browser_driver: BrowserDriver, xpath: str, timeout: float) -> bool:
    xpath = XPath(xpath)
    driver = browser_driver.get_webdriver()
    try:
        element: object = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))  # type: ignore
        return element is not None
    except (TimeoutException, NoSuchElementException, Exception):
        return False
