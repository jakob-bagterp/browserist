from .... import helper_iteration
from ....model.type.xpath import XPath
from ...check_if.is_clickable import check_if_is_clickable


def wait_until_element_is_clickable(driver: object, xpath: str, timeout: float) -> None:
    xpath = XPath(xpath)
    helper_iteration.retry.until_condition_is_true(driver, xpath, func=check_if_is_clickable, timeout=timeout)
