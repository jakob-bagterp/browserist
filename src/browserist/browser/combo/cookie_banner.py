import time

from ... import constant
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ...model.combo_settings.handling_state import ComboHandlingState, IsComboHandled
from ...model.driver_methods import DriverMethods
from ...model.type.callable import TimeoutShouldContinueCallable
from ..check_if.is_displayed import check_if_is_displayed
from ..click.button import click_button, click_button_without_wait
from ..iframe.switch_to import switch_to_iframe
from ..iframe.switch_to_original_page import switch_to_original_page
from ..open.url import open_url
from ..wait.for_element import wait_for_element
from ..wait.until.element_disappears import wait_until_element_disappears


def combo_cookie_banner(
    driver_method: DriverMethods, cookie_banner: CookieBannerSettings, timeout: float
) -> bool | None:
    timeout_should_continue: TimeoutShouldContinueCallable = driver_method._timeout_should_continue
    browser_driver = driver_method._browser_driver
    handling_state = ComboHandlingState()
    return_bool_value: bool | None = None

    def load_cookie_banner() -> None:
        if cookie_banner.url is not None and timeout_should_continue():
            open_url(browser_driver, cookie_banner.url)
        if cookie_banner.iframe_xpath is not None and timeout_should_continue():
            switch_to_iframe(browser_driver, cookie_banner.iframe_xpath, timeout)
        if cookie_banner.has_loaded_wait_seconds is not None:
            time.sleep(cookie_banner.has_loaded_wait_seconds)
        if cookie_banner.has_loaded_xpath is not None and timeout_should_continue():
            wait_for_element(browser_driver, cookie_banner.has_loaded_xpath, timeout)

    def click_cookie_banner_button() -> None:
        if timeout_should_continue():
            click_button(browser_driver, cookie_banner.button_xpath, timeout)

    def click_cookie_banner_button_and_handle_return_bool() -> None:
        if timeout_should_continue():
            wait_for_element(browser_driver, cookie_banner.button_xpath, timeout)
            if check_if_is_displayed(browser_driver, cookie_banner.button_xpath):
                handling_state.set(IsComboHandled.NOT_YET_BUT_SOON)
            click_button_without_wait(browser_driver, cookie_banner.button_xpath)  # type: ignore

    def wait_for_cookie_banner_to_disappear_by_time() -> None:  # This also allows any cookie values to be saved.
        if cookie_banner.has_disappeared_wait_seconds is not None:
            time.sleep(cookie_banner.has_disappeared_wait_seconds)
        else:
            time.sleep(constant.timeout.VERY_SHORT)

    def wait_for_cookie_banner_to_disappear_by_element() -> None:
        if timeout_should_continue():
            wait_until_element_disappears(browser_driver, cookie_banner.button_xpath, timeout)

    def wait_for_cookie_banner_to_disappear_by_element_and_handle_return_bool() -> None:
        if timeout_should_continue():
            wait_until_element_disappears(browser_driver, cookie_banner.button_xpath, timeout)
            if handling_state.get() is not IsComboHandled.NOT_STARTED and not check_if_is_displayed(
                browser_driver, cookie_banner.button_xpath
            ):
                handling_state.set(IsComboHandled.YES_AND_WITH_SUCCESS)

    def reset_cookie_banner_iframe_if_needed() -> None:
        if cookie_banner.iframe_xpath is not None and timeout_should_continue():
            switch_to_original_page(browser_driver)

    def flow_without_return_bool() -> None:
        click_cookie_banner_button()
        wait_for_cookie_banner_to_disappear_by_time()
        wait_for_cookie_banner_to_disappear_by_element()
        reset_cookie_banner_iframe_if_needed()

    def flow_with_return_bool() -> bool | None:
        try:
            click_cookie_banner_button_and_handle_return_bool()
            wait_for_cookie_banner_to_disappear_by_time()
            wait_for_cookie_banner_to_disappear_by_element_and_handle_return_bool()
            reset_cookie_banner_iframe_if_needed()
            return handling_state.get_value()
        except Exception:
            return False

    load_cookie_banner()
    if cookie_banner.return_bool:
        return_bool_value = flow_with_return_bool()
    else:
        flow_without_return_bool()
    return return_bool_value
