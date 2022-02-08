import time
from .click import click_button
from .input import input_value
from .open import open_url_if_not_current
from .wait import wait_until_element_disappears, wait_until_url_contains
from .wait_for_element import wait_for_element
from ..constant import timeout
from ..exception.cookie_banner import CookieBannerException
from ..exception.login import LoginException
from ..model.browser.base.driver import BrowserDriver
from ..model.cookie_banner import CookieBannerSettings
from ..model.driver_methods import DriverMethods
from ..model.login import LoginCredentials, LoginForm

def combo_cookie_banner(driver: object, settings: CookieBannerSettings) -> None:
    try:
        if settings.url is not None:
            open_url_if_not_current(driver, settings.url)
        time.sleep(settings.has_loaded_wait_seconds)
        if settings.has_loaded_xpath is not None:
            wait_for_element(driver, settings.has_loaded_xpath)
        click_button(driver, settings.button_xpath)
        time.sleep(settings.has_disappeared_wait_seconds)
        wait_until_element_disappears(driver, settings.button_xpath)
    except Exception:
        raise CookieBannerException()

def combo_login(driver: object, login_credentials: LoginCredentials, login_form: LoginForm, wait_seconds: int = timeout.DEFAULT) -> None:
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
        raise LoginException(login_credentials.username)

class ComboDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        
    def cookie_banner(self, settings: CookieBannerSettings) -> None:
        """Standardised combination of methods to accept or decline cookies."""

        combo_cookie_banner(self._driver, settings)

    def login(self, login_credentials: LoginCredentials, login_form: LoginForm, wait_seconds: int = timeout.DEFAULT) -> None:
        """Standardised combination of methods to log in.

        wait_seconds: Extra seconds in addition to timeout to make sure the login is processed and that the user is redirected succesfully."""

        combo_login(self._driver, login_credentials, login_form, wait_seconds)
