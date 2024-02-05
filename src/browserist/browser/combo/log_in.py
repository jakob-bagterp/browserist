import time

from ...model.combo_settings.login_credentials import LoginCredentials
from ...model.combo_settings.login_form import LoginForm1Step, LoginForm2Steps
from ...model.driver_methods import DriverMethods
from ...model.type.callable import TimeoutShouldContinueCallable
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.url.contains import wait_until_url_contains


def combo_log_in(driver_method: DriverMethods, login_credentials: LoginCredentials, login_form: LoginForm1Step | LoginForm2Steps, timeout: float) -> None:
    timeout_should_continue: TimeoutShouldContinueCallable = driver_method._timeout_should_continue
    browser_driver = driver_method._browser_driver

    def login_form_1_step(login_form: LoginForm1Step) -> None:
        if timeout_should_continue():
            input_value(browser_driver, login_form.username_input_xpath, login_credentials.username, timeout)
        if timeout_should_continue():
            input_value(browser_driver, login_form.password_input_xpath, login_credentials.password, timeout)
        if timeout_should_continue():
            click_button(browser_driver, login_form.submit_button_xpath, timeout)

    def login_form_2_steps(login_form: LoginForm2Steps) -> None:
        if timeout_should_continue():
            input_value(browser_driver, login_form.username_input_xpath, login_credentials.username, timeout)
        if timeout_should_continue():
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

    if login_form.url is not None and timeout_should_continue():
        open_url_if_not_current(browser_driver, login_form.url)

    match login_form:
        case LoginForm1Step():
            login_form_1_step(login_form)
        case LoginForm2Steps():
            login_form_2_steps(login_form)

    post_login_flow(login_form)
