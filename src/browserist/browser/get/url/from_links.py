from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ..attribute.values import get_attribute_values


def get_url_from_links(browser_driver: BrowserDriver, xpath: str, timeout: float) -> list[str | None]:
    xpath = XPath(xpath)
    return get_attribute_values(browser_driver, xpath, "href", timeout)
