from selenium.webdriver.support import expected_conditions

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait


def check_if_is_clickable(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        element = get_element_without_wait(browser_driver, xpath)
        return bool(expected_conditions.element_to_be_clickable(element))
    except Exception:
        return False
