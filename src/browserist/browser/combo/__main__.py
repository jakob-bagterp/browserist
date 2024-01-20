from ...model.browser.base.driver import BrowserDriver
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ...model.combo_settings.login_credentials import LoginCredentials
from ...model.combo_settings.login_form import LoginForm1Step, LoginForm2Steps
from ...model.combo_settings.search import SearchSettings
from ...model.driver_methods import DriverMethods
from .cookie_banner import combo_cookie_banner
from .log_in import combo_log_in
from .search import combo_search


class ComboDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def cookie_banner(self, settings: CookieBannerSettings, timeout: float | None = None) -> None:
        """Standardised combination of methods to accept or decline cookies.

        Args:
            settings (CookieBannerSettings): Add settings class.
            timeout (float | None, optional): In seconds. Timeout to wait for element(s). If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1"
            from browserist import Browser, CookieBannerSettings

            accept_cookies = CookieBannerSettings(
                url = "https://example.com",
                has_loaded_xpath = "//xpath/to/cookie_banner",
                button_xpath = "//xpath/to/accept_button")

            with Browser() as browser:
                browser.combo.cookie_banner(accept_cookies)
                browser.open.url("https://example.com/some_page")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            combo_cookie_banner(self, settings, timeout)

    def log_in(self, login_credentials: LoginCredentials, login_form: LoginForm1Step | LoginForm2Steps, timeout: float | None = None) -> None:
        """Standardised combination of methods to log in.

        Note:
            Most websites process login in either one or two steps.
            Use `LoginForm1Step` when username and password are prompted on the same page.
            Use `LoginForm2Steps` when username is prompted first, and then the option to input password appears later on the same or a separate page. The two-step variation is often to verify whether a user exists or not before password can be entered (or should be redirected to a registration page).

        Args:
            login_credentials (LoginCredentials): Apply username and password here.
            login_form (LoginForm1Step | LoginForm2Steps): Add settings class.
            timeout (float | None, optional): In seconds. Timeout to wait for element(s). If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1"
            from browserist import Browser, LoginForm1Step, LoginCredentials

            login_credentials = LoginCredentials(
                username = "some_username",
                password = "some_password")

            login_form = LoginForm1Step(
                url = "https://example.com/login",
                username_input_xpath = "//xpath/to/username_field",
                password_input_xpath = "//xpath/to/password_field",
                submit_button_xpath = "//xpath/to/login_button")

            with Browser() as browser:
                browser.combo.log_in(login_credentials, login_form)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            combo_log_in(self, login_credentials, login_form, timeout)

    def search(self, term: str, settings: SearchSettings, timeout: float | None = None) -> None:
        """Standardised combination of methods to perform search.

        Args:
            term (str): Terms to search for.
            settings (SearchSettings): Add settings class.
            timeout (float | None, optional): In seconds. Timeout to wait for element(s). If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1"
            from browserist import Browser, SearchSettings

            search_settings = SearchSettings(
                url = "https://google.com",
                input_xpath = "//xpath/to/input_field",
                button_xpath = "//xpath/to/search_button")

            with Browser() as browser:
                browser.combo.search("some search term", search_settings)
                assert browser.tool.count_elements("//xpath/to/search_result_elements") > 0
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            combo_search(self, term, settings, timeout)
