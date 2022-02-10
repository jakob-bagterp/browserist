from ..check_if.does_element_exist import check_if_does_element_exist
from ... import helper
from ...constant import timeout

def wait_until_element_disappears(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    helper.retry.until_condition_is_false(check_if_does_element_exist(driver, xpath), timeout)
