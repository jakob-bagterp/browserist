from ....model.browser.base.driver import BrowserDriver
from ..element import get_element


def get_element_inner_html(browser_driver: BrowserDriver, xpath: str, timeout: float) -> str:
    element = get_element(browser_driver, xpath, timeout)
    return str(element.get_attribute("innerHTML"))
