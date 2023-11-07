from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...get.element import get_element_without_wait
from ...wait.for_element import wait_for_element


def get_attribute_value(browser_driver: BrowserDriver, xpath: str, attribute: str, timeout: float) -> str | None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    element = get_element_without_wait(browser_driver, xpath)
    return element.get_attribute(attribute)
