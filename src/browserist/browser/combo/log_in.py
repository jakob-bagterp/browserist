import time

from browserist.browser.check_if.is_displayed import check_if_is_displayed
from browserist.browser.get.url.current import get_current_url

from ...model.combo_settings.handling_state import ComboHandlingState, IsComboHandled
from ...model.combo_settings.login_credentials import LoginCredentials
from ...model.combo_settings.login_form import LoginForm1Step, LoginForm2Steps
from ...model.driver_methods import DriverMethods
from ...model.type.callable import TimeoutShouldContinueCallable
from ..click.button import click_button
from ..input.value import input_value
from ..open.url import open_url
from ..wait.for_element import wait_for_element
from ..wait.until.url.contains import wait_until_url_contains


def combo_log_in(
    driver_method: DriverMethods,
    login_credentials: LoginCredentials,
    login_form: LoginForm1Step | LoginForm2Steps,
    timeout: float,
) -> bool | None:
    timeout_should_continue: TimeoutShouldContinueCallable = driver_method._timeout_should_continue
    browser_driver = driver_method._browser_driver
    handling_state = ComboHandlingState()
    return_bool_value: bool | None = None

    def login_form_1_step(login_form: LoginForm1Step) -> None:
        if timeout_should_continue():
            input_value(browser_driver, login_form.username_input_xpath, login_credentials.username, timeout)
        if timeout_should_continue():
            input_value(browser_driver, login_form.password_input_xpath, login_credentials.password, timeout)
        if timeout_should_continue():
            handling_state.set(IsComboHandled.NOT_YET_BUT_SOON)
            click_button(browser_driver, login_form.submit_button_xpath, timeout)

    def login_form_2_steps(login_form: LoginForm2Steps) -> None:
        if timeout_should_continue():
            input_value(browser_driver, login_form.username_input_xpath, login_credentials.username, timeout)
        if timeout_should_continue():
            handling_state.set(IsComboHandled.NOT_YET_BUT_SOON)
            click_button(browser_driver, login_form.username_submit_button_xpath, timeout)
        if timeout_should_continue():
            input_value(browser_driver, login_form.password_input_xpath, login_credentials.password, timeout)
        if timeout_should_continue():
            click_button(browser_driver, login_form.password_submit_button_xpath, timeout)

    def post_login_flow(login_form: LoginForm1Step | LoginForm2Steps) -> None:
        if login_form.post_login_wait_seconds is not None:
            time.sleep(login_form.post_login_wait_seconds)
        if login_form.post_login_url_contains is not None and timeout_should_continue():
            wait_until_url_contains(browser_driver, login_form.post_login_url_contains, timeout)
        if login_form.post_login_element_xpath is not None and timeout_should_continue():
            wait_for_element(browser_driver, login_form.post_login_element_xpath, timeout)

    def post_login_flow_and_handle_return_bool(login_form: LoginForm1Step | LoginForm2Steps) -> None:
        def does_post_login_url_contain() -> bool:
            if login_form.post_login_url_contains is not None:
                return login_form.post_login_url_contains in get_current_url(browser_driver)
            else:
                return False

        def is_post_login_element_displayed() -> bool:
            if login_form.post_login_element_xpath is not None:
                return check_if_is_displayed(browser_driver, login_form.post_login_element_xpath)
            else:
                return False

        post_login_flow(login_form)
        if handling_state.get() is not IsComboHandled.NOT_STARTED and any(
            [does_post_login_url_contain(), is_post_login_element_displayed()]
        ):
            handling_state.set(IsComboHandled.YES_AND_WITH_SUCCESS)

    def flow_login_form_1_step_without_return_bool(login_form: LoginForm1Step) -> None:
        login_form_1_step(login_form)
        post_login_flow(login_form)

    def flow_login_form_1_step_with_return_bool(login_form: LoginForm1Step) -> bool | None:
        try:
            login_form_1_step(login_form)
            post_login_flow_and_handle_return_bool(login_form)
            return handling_state.get_value()
        except Exception:
            return False

    def flow_login_form_2_steps_without_return_bool(login_form: LoginForm2Steps) -> None:
        login_form_2_steps(login_form)
        post_login_flow(login_form)

    def flow_login_form_2_steps_with_return_bool(login_form: LoginForm2Steps) -> bool | None:
        try:
            login_form_2_steps(login_form)
            post_login_flow_and_handle_return_bool(login_form)
            return handling_state.get_value()
        except Exception:
            return False

    if login_form.url is not None and timeout_should_continue():
        open_url(browser_driver, login_form.url)
    match login_form:
        case LoginForm1Step():
            if login_form.return_bool:
                return_bool_value = flow_login_form_1_step_with_return_bool(login_form)
            else:
                flow_login_form_1_step_without_return_bool(login_form)
        case LoginForm2Steps():
            if login_form.return_bool:
                return_bool_value = flow_login_form_2_steps_with_return_bool(login_form)
            else:
                flow_login_form_2_steps_without_return_bool(login_form)
    return return_bool_value
