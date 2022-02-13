import time
from ..click.button import click_button
from ..input.value import input_value
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.until_url_contains import wait_until_url_contains
from ..wait.for_element import wait_for_element
from ...constant import timeout
from ...exception.login import LoginException
from ...model.combo_settings.login import LoginCredentials, LoginForm

def combo_log_in(driver: object, login_credentials: LoginCredentials, login_form: LoginForm, wait_seconds: int = timeout.DEFAULT) -> None:
    try:
        if login_form.url is not None:
            open_url_if_not_current(driver, login_form.url)
        input_value(driver, login_form.username_input_xpath, login_credentials.username)
        input_value(driver, login_form.password_input_xpath, login_credentials.password)
        click_button(driver, login_form.submit_button_xpath)
        time.sleep(wait_seconds)
        if login_form.post_login_url is not None:
            wait_until_url_contains(driver, login_form.post_login_url)
        if login_form.post_login_element_xpath is not None:
            wait_for_element(driver, login_form.post_login_element_xpath)
    except Exception:
        raise LoginException(login_credentials.username) from Exception
