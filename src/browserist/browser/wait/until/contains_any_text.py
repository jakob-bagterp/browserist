from .... import helper
from ....constant import timeout
from ....model.type.xpath import XPath
from ...check_if.contains_any_text import check_if_contains_any_text


def wait_until_element_contains_any_text(driver: object, xpath: str, timeout: float = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    helper.retry.until_condition_is_true(driver, xpath, func=check_if_contains_any_text, timeout=timeout)
