from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait


def check_if_is_displayed(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        element = get_element_without_wait(browser_driver, xpath)
        return bool(element.is_displayed())
    except Exception:
        return False
