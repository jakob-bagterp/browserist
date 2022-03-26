from .... import constant, helper
from ....constant import timeout
from ....model.type.xpath import XPath
from ...wait.for_element import wait_for_element
from ..attribute.value import get_attribute_value


def get_url_from_image(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_src_attribute_of_element(driver: object, xpath: str) -> str:
        return get_attribute_value(driver, xpath, "src", constant.timeout.BYPASS)

    xpath = XPath(xpath)
    wait_for_element(driver, xpath, timeout)
    return helper.retry.get_text_from_element(driver, xpath, get_src_attribute_of_element)
