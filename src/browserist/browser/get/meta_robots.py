from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait

META_ROBOTS_XPATH = XPath("/html/head/meta[@name='robots']")


def get_meta_robots(browser_driver: BrowserDriver) -> str:
    try:
        element = get_element_without_wait(browser_driver, META_ROBOTS_XPATH)
        return str(element.get_attribute("content")) if element else ""
    except Exception:
        return ""
