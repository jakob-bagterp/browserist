import time

from ...exception.login import LoginException
from ...model.combo_settings.login_credentials import LoginCredentials
from ...model.combo_settings.login_form import LoginForm1Step, LoginForm2Steps
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until_url_contains import wait_until_url_contains


def combo_log_in(driver: object, login_credentials: LoginCredentials, login_form: LoginForm1Step | LoginForm2Steps) -> None:
    def login_form_1_step(login_form: LoginForm1Step) -> None:
        input_value(driver, login_form.username_input_xpath, login_credentials.username)
        input_value(driver, login_form.password_input_xpath, login_credentials.password)
        click_button(driver, login_form.submit_button_xpath)

    def login_form_2_steps(login_form: LoginForm2Steps) -> None:
        input_value(driver, login_form.username_input_xpath, login_credentials.username)
        click_button(driver, login_form.username_submit_button_xpath)
        input_value(driver, login_form.password_input_xpath, login_credentials.password)
        click_button(driver, login_form.password_submit_button_xpath)

    try:
        if login_form.url is not None:
            open_url_if_not_current(driver, login_form.url)

        if type(login_form) is LoginForm1Step:
            login_form_1_step(login_form)
        elif type(login_form) is LoginForm2Steps:
            login_form_2_steps(login_form)

        if login_form.post_login_wait_seconds is not None:
            time.sleep(login_form.post_login_wait_seconds)
        if login_form.post_login_url is not None:
            wait_until_url_contains(driver, login_form.post_login_url)
        if login_form.post_login_element_xpath is not None:
            wait_for_element(driver, login_form.post_login_element_xpath)
    except Exception:
        raise LoginException(login_credentials.username) from Exception
