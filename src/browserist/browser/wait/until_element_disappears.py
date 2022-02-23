from ... import helper
from ...constant import timeout
from ..check_if.is_element_displayed import check_if_is_element_displayed


def wait_until_element_disappears(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    helper.retry.until_condition_is_false(check_if_is_element_displayed(driver, xpath), timeout)
