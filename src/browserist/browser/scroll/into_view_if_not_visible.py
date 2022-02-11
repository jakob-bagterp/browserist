from .into_view import scroll_into_view
from ..check_if.is_element_visible import check_if_is_element_visible
from ...constant import timeout

def scroll_into_view_if_not_visible(driver: object, xpath: str, timeout: int = timeout.DEFAULT) -> None:
    if not check_if_is_element_visible(driver, xpath):
        scroll_into_view(driver, xpath, timeout)
