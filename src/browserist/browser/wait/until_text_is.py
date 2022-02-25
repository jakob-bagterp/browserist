import re

from ... import constant, helper
from ...constant import timeout
from ..get.text.from_element import get_text_from_element
from .for_element import wait_for_element


def wait_until_text_is(driver: object, xpath: str, regex: str, timeout: int = timeout.DEFAULT) -> None:
    def is_element_text(driver: object, xpath: str, regex: str) -> bool:
        text = get_text_from_element(driver, xpath, constant.timeout.BYPASS)
        return bool(re.match(regex, text))

    wait_for_element(driver, xpath, timeout)
    helper.retry.until_condition_is_true(is_element_text(driver, xpath, regex), timeout)
