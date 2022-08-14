from selenium.webdriver.common.by import By

from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath


def check_if_is_image_loaded(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        driver = browser_driver.get_webdriver()
        element = driver.find_element(By.XPATH, xpath)  # type: ignore
        return helper.image.is_element_loaded(driver, element)
    except Exception:
        return False
