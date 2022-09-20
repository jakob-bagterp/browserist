from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait


def check_if_is_image_loaded(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        driver = browser_driver.get_webdriver()
        element = get_element_without_wait(browser_driver, xpath)
        return helper.image.is_element_loaded(driver, element)
    except Exception:
        return False
