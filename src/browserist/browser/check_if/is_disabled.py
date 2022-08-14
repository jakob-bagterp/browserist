from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from .is_enabled import check_if_is_enabled


def check_if_is_disabled(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    return not check_if_is_enabled(browser_driver, xpath)
