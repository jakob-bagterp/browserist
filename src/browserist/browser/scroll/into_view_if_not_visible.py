from ...constant import timeout
from ...model.type.xpath import XPath
from ..check_if.is_element_displayed import check_if_is_element_displayed
from .into_view import scroll_into_view


def scroll_into_view_if_not_visible(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    xpath = XPath(xpath)
    if not check_if_is_element_displayed(driver, xpath):
        scroll_into_view(driver, xpath, timeout)
