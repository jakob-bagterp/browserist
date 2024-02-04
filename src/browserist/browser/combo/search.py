from ...model.combo_settings.search import SearchSettings
from ...model.driver_methods import DriverMethods
from ...model.type.callable import TimeoutShouldContinueCallable
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.url.contains import wait_until_url_contains


def combo_search(driver_method: DriverMethods, term: str, search: SearchSettings, timeout: float) -> None:
    timeout_should_continue: TimeoutShouldContinueCallable = driver_method._timeout_should_continue
    browser_driver = driver_method._browser_driver

    if search.url is not None and timeout_should_continue():
        open_url_if_not_current(browser_driver, search.url)
    if timeout_should_continue():
        input_value(browser_driver, search.input_xpath, term, timeout)
    if timeout_should_continue():
        click_button(browser_driver, search.button_xpath, timeout)
    if search.await_search_results_url_contains is not None and timeout_should_continue():
        wait_until_url_contains(browser_driver, search.await_search_results_url_contains, timeout)
    if search.await_search_results_xpath is not None and timeout_should_continue():
        wait_for_element(browser_driver, search.await_search_results_xpath, timeout)
