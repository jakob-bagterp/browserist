from ...exception.search import SearchException
from ...model.combo_settings.search import SearchSettings
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until_url_contains import wait_until_url_contains


def combo_search(driver: object, term: str, settings: SearchSettings) -> None:
    try:
        if settings.url is not None:
            open_url_if_not_current(driver, settings.url)
        input_value(driver, settings.input_xpath, term)
        click_button(driver, settings.button_xpath)
        if settings.await_search_results_url is not None:
            wait_until_url_contains(driver, settings.await_search_results_url)
        if settings.await_search_results_xpath is not None:
            wait_for_element(driver, settings.await_search_results_xpath)
    except Exception:
        raise SearchException(term) from Exception
