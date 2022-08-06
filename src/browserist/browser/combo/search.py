from ...model.combo_settings.search import SearchSettings
from ...model.driver_methods import DriverMethods
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.url.contains import wait_until_url_contains


def combo_search(driver_method: DriverMethods, term: str, search: SearchSettings, timeout: int) -> None:
    if search.url is not None and driver_method._timeout_should_continue():
        open_url_if_not_current(driver_method._browser_driver, search.url)
    if driver_method._timeout_should_continue():
        input_value(driver_method._browser_driver, search.input_xpath, term, timeout)
    if driver_method._timeout_should_continue():
        click_button(driver_method._browser_driver, search.button_xpath, timeout)
    if search.await_search_results_url_contains is not None and driver_method._timeout_should_continue():
        wait_until_url_contains(driver_method._browser_driver, search.await_search_results_url_contains, timeout)
    if search.await_search_results_xpath is not None and driver_method._timeout_should_continue():
        wait_for_element(driver_method._browser_driver, search.await_search_results_xpath, timeout)
