from .... import iteration_helper
from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...check_if.is_displayed import check_if_is_displayed


def wait_until_element_disappears(browser_driver: BrowserDriver, xpath: str, timeout: int) -> None:
    xpath = XPath(xpath)
    iteration_helper.retry.until_condition_is_false_without_browser_settings(
        browser_driver.webdriver, xpath, func=check_if_is_displayed, timeout=timeout)
