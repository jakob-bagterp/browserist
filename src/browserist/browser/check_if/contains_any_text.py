from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait


def check_if_contains_any_text(browser_driver: BrowserDriver, xpath: str) -> bool:
    xpath = XPath(xpath)
    try:
        element = get_element_without_wait(browser_driver, xpath)
        text = str(element.text)
        return bool(text)
    except Exception:
        return False
