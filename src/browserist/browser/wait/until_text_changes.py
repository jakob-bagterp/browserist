from ... import helper
from ...constant import timeout
from ..get.text.from_element import get_text_from_element
from .for_element import wait_for_element


def wait_until_text_changes(driver: object, xpath: str, baseline_text: str, timeout: int = timeout.DEFAULT) -> None:
    def has_text_changed(driver: object, baseline_text: str) -> bool:
        return get_text_from_element(driver, xpath) != baseline_text

    wait_for_element(driver, xpath, timeout)
    helper.retry.until_condition_is_true(has_text_changed(driver, baseline_text), timeout)
