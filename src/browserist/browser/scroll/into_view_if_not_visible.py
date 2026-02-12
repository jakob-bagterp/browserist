from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..check_if.is_in_viewport import check_if_is_in_viewport
from .into_view import scroll_into_view


def scroll_into_view_if_not_in_viewport(
    browser_driver: BrowserDriver, xpath: str, timeout: float, delay_seconds: float
) -> None:
    xpath = XPath(xpath)
    if not check_if_is_in_viewport(browser_driver, xpath):
        scroll_into_view(browser_driver, xpath, timeout, delay_seconds)
