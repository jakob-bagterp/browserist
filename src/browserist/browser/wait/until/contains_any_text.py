from .... import helper_iteration
from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...check_if.contains_any_text import check_if_contains_any_text


def wait_until_element_contains_any_text(browser_driver: BrowserDriver, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    helper_iteration.retry.until_condition_is_true(
        browser_driver, xpath, func=check_if_contains_any_text, timeout=timeout
    )
