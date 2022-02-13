import re
from .for_element import wait_for_element
from ..get.text.from_element import get_text_from_element
from ...constant import timeout
from ... import helper
from ... import constant

def wait_until_text_contains(driver: object, xpath: str, regex: str, timeout: int = timeout.DEFAULT) -> None:
    def does_element_text_contain(driver: object, xpath: str, regex: str) -> bool:
        text = get_text_from_element(driver, xpath, constant.timeout.BYPASS)
        return bool(re.search(regex, text, re.IGNORECASE))

    wait_for_element(driver, xpath, timeout)
    helper.retry.until_condition_is_true(does_element_text_contain(driver, xpath, regex), timeout)
