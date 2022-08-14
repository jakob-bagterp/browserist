from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore

from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_is_clickable(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        driver = browser_driver.get_webdriver()
        element = WebDriverWait(driver, timeout.BYPASS).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))  # type: ignore
        return element is not None
    except Exception:
        return False
