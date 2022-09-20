from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.elements import get_elements_without_wait
from ..wait.for_element import wait_for_element


def tool_count_elements(browser_driver: BrowserDriver, xpath: str, timeout: float) -> int:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    elements = get_elements_without_wait(browser_driver, xpath)
    return len(elements)
