from ....model.browser.base.driver import BrowserDriver
from ....model.type.xpath import XPath
from ...get.element import get_element_without_wait

CANONICAL_URL_XPATH = XPath("/html/head/link[@rel='canonical']")


def get_canonical_url(browser_driver: BrowserDriver) -> str | None:
    try:
        element = get_element_without_wait(browser_driver, CANONICAL_URL_XPATH)
        return str(element.get_attribute("href")) if element else None
    except Exception:
        return None
