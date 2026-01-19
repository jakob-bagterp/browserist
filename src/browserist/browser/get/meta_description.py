from ...model.browser.base.driver import BrowserDriver
from ...model.type.xpath import XPath
from ..get.element import get_element_without_wait

META_DESCRIPTION_XPATH = XPath("/html/head/meta[@name='description']")


def get_meta_description(browser_driver: BrowserDriver) -> str:
    try:
        element = get_element_without_wait(browser_driver, META_DESCRIPTION_XPATH)
        return str(element.get_attribute("content")) if element else ""
    except Exception:
        return ""
