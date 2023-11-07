from ... import helper_iteration
from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait
from ..wait.for_element import wait_for_element


def get_text(browser_driver: BrowserDriver, xpath: str, timeout: float) -> str:
    def get_inner_text_of_element(browser_driver: BrowserDriver, xpath: XPath) -> str:
        element = get_element_without_wait(browser_driver, xpath)
        return str(element.text)

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    text = helper_iteration.retry.get_text(browser_driver, xpath, get_inner_text_of_element)
    return text if text is not None else ""
