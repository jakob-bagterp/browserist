from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait
from ..wait.for_element import wait_for_element


def select_input_field(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    element = get_element_without_wait(browser_driver, xpath)
    element.click()
