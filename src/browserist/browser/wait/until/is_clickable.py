from .... import helper_iteration
from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...check_if.is_clickable import check_if_is_clickable


def wait_until_element_is_clickable(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    helper_iteration.retry.until_condition_is_true(browser_driver, xpath, func=check_if_is_clickable, timeout=timeout)
