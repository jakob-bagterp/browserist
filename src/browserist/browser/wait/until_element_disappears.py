from ... import helper
from ...constant import timeout
from ...model.type.xpath import XPath
from ..check_if.is_element_displayed import check_if_is_element_displayed


def wait_until_element_disappears(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    helper.retry.until_condition_is_false(driver, xpath, func=check_if_is_element_displayed, timeout=timeout)
