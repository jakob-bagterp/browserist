from .... import helper_iteration
from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...check_if.is_displayed import check_if_is_displayed


def wait_until_element_disappears(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    helper_iteration.retry.until_condition_is_false(browser_driver, xpath, func=check_if_is_displayed, timeout=timeout)
