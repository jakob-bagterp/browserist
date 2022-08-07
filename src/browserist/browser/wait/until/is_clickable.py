from .... import helper
from ....constant import timeout
from ....model.type.xpath import XPath
from ...check_if.is_clickable import check_if_is_clickable


def wait_until_element_is_clickable(driver: object, xpath: str, timeout: float = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    helper.retry.until_condition_is_true(driver, xpath, func=check_if_is_clickable, timeout=timeout)
