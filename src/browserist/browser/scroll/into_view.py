import time

from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait
from ..tool.execute_script import tool_execute_script
from ..wait.for_element import wait_for_element


def scroll_into_view(browser_driver: BrowserDriver, xpath: str, timeout: float, delay_seconds: float) -> None:
    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    element = get_element_without_wait(browser_driver, xpath)
    tool_execute_script(browser_driver, "arguments[0].scrollIntoView();", element)
    time.sleep(delay_seconds)  # Small delay to ensure that the screen is updated after scroll.
