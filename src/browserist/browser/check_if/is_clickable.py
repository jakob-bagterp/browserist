from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_is_clickable(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        driver = browser_driver.get_webdriver()
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return bool(EC.element_to_be_clickable(element))  # type: ignore
    except Exception:
        return False
