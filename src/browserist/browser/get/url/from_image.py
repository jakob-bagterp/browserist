from .... import constant, helper
from ....model.browser.base.settings import BrowserSettings
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element
from ..attribute.value import get_attribute_value


def get_url_from_image(driver: object, settings: BrowserSettings, xpath: str, timeout: int) -> str:
    def get_src_attribute_of_element(driver: object, settings: BrowserSettings, xpath: str) -> str:
        return get_attribute_value(driver, settings, xpath, "src", constant.timeout.BYPASS)

    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    return helper.retry.get_text(driver, settings, xpath, get_src_attribute_of_element)
