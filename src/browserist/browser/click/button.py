from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait
from ..wait.for_element import wait_for_element


def click_button(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    click_button_without_wait(browser_driver, xpath)


def click_button_without_wait(browser_driver: BrowserDriver, xpath: XPath) -> None:
    """Variation of the click_button() method for internal use only. It assumes that the XPath has already been validated."""

    element = get_element_without_wait(browser_driver, xpath)
    element.click()
