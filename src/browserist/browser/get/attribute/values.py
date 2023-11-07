from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...get.elements import get_elements_without_wait
from ...wait.for_element import wait_for_element


def get_attribute_values(browser_driver: BrowserDriver, xpath: str, attribute: str, timeout: float) -> list[str | None]:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    elements = get_elements_without_wait(browser_driver, xpath)
    return [element.get_attribute(attribute) for element in elements]
