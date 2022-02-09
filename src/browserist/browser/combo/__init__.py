__all__ = []

from .cookie_banner import combo_cookie_banner
from .log_in import combo_log_in
from ...constant import timeout
from ...model.browser.base.driver import BrowserDriver
from ...model.cookie_banner import CookieBannerSettings
from ...model.driver_methods import DriverMethods
from ...model.login import LoginCredentials, LoginForm

class ComboDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)
        
    def cookie_banner(self, settings: CookieBannerSettings) -> None:
        """Standardised combination of methods to accept or decline cookies."""

        combo_cookie_banner(self._driver, settings)

    def log_in(self, login_credentials: LoginCredentials, login_form: LoginForm, wait_seconds: int = timeout.DEFAULT) -> None:
        """Standardised combination of methods to log in.

        wait_seconds: Extra seconds in addition to timeout to make sure the login is processed and that the user is redirected succesfully."""

        combo_log_in(self._driver, login_credentials, login_form, wait_seconds)
