from .value_from_attribute import get_value_from_attribute
from ..wait.for_element import wait_for_element
from ... import constant
from ... import helper
from ...constant import timeout

def get_url_from_link(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> str:
    def get_href_attribute_of_element(driver: object, xpath: str) -> str:
        return get_value_from_attribute(driver, xpath, "href", constant.timeout.BYPASS)

    wait_for_element(driver, xpath, timeout)
    return helper.driver.retry_and_get_text_from_element(get_href_attribute_of_element(driver, xpath))
