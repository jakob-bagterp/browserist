from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.elements import get_elements_without_wait
from ..wait.for_element import wait_for_element


def get_texts(browser_driver: BrowserDriver, xpath: str, timeout: float) -> list[str]:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    elements = get_elements_without_wait(browser_driver, xpath)
    return [element.text for element in elements]
