from selenium.webdriver.common.by import By

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_contains_any_text(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        driver = browser_driver.get_webdriver()
        text = str(driver.find_element(By.XPATH, xpath).text)  # type: ignore
        return bool(text)
    except Exception:
        return False
