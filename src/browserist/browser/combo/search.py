from ...constant import timeout
from ...model.browser.base.settings import BrowserSettings
from ...model.combo_settings.search import SearchSettings
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.url.contains import wait_until_url_contains


def combo_search(driver: object, settings: BrowserSettings, term: str, search: SearchSettings) -> None:
    # TODO: Incorporate timeout strategy and settings
    # TODO: Handle timeout.DEFAULT in alignment with timeout strategy and settings

    if search.url is not None:
        open_url_if_not_current(driver, search.url)
    input_value(driver, settings, search.input_xpath, term, timeout.DEFAULT)
    click_button(driver, settings, search.button_xpath, timeout.DEFAULT)
    if search.await_search_results_url_contains is not None:
        wait_until_url_contains(driver, search.await_search_results_url_contains, timeout.DEFAULT)
    if search.await_search_results_xpath is not None:
        wait_for_element(driver, settings, search.await_search_results_xpath, timeout.DEFAULT)
