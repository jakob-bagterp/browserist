from ...model.browser.base.driver import BrowserDriver
from ...model.browser.base.settings import BrowserSettings
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ...model.combo_settings.login_credentials import LoginCredentials
from ...model.combo_settings.login_form import LoginForm1Step, LoginForm2Steps
from ...model.combo_settings.search import SearchSettings
from ...model.driver_methods import DriverMethods
from .cookie_banner import combo_cookie_banner
from .log_in import combo_log_in
from .search import combo_search


class ComboDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def cookie_banner(self, settings: CookieBannerSettings) -> None:
        """Standardised combination of methods to accept or decline cookies."""

        combo_cookie_banner(self._driver, settings)

    def log_in(self, login_credentials: LoginCredentials, login_form: LoginForm1Step | LoginForm2Steps) -> None:
        """Standardised combination of methods to log in.

        wait_seconds: Extra seconds in addition to timeout to make sure the login is processed and that the user is redirected succesfully."""

        combo_log_in(self._driver, login_credentials, login_form)

    def search(self, term: str, settings: SearchSettings) -> None:
        """Standardised combination of methods to perform search."""

        combo_search(self._driver, term, settings)
