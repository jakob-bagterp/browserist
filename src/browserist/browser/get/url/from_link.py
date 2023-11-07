from .... import constant, helper_iteration
from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element
from ..attribute.value import get_attribute_value


def get_url_from_link(browser_driver: BrowserDriver, xpath: str, timeout: float) -> str | None:
    def get_href_attribute_of_element(browser_driver: BrowserDriver, xpath: str) -> str | None:
        return get_attribute_value(browser_driver, xpath, "href", constant.timeout.BYPASS)

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    return helper_iteration.retry.get_text(browser_driver, xpath, get_href_attribute_of_element)
