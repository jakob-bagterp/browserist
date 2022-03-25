from dataclasses import dataclass


@dataclass
class _LoginFormInput:
    """Shared for input values for login form."""

    username_input_xpath: str
    password_input_xpath: str


@dataclass
class _LoginForm1Step:
    """Specific input value for 1 step login flow."""

    submit_button_xpath: str


@dataclass
class _LoginForm2Steps:
    """Specific input values for 2 steps login flow."""

    username_submit_button_xpath: str
    password_submit_button_xpath: str


@dataclass
class _LoginFormSharedDefaults:
    """Base class with shared, default values."""

    url: str | None = None
    post_login_wait_seconds: int | None = None
    post_login_url: str | None = None
    post_login_element_xpath: str | None = None


class LoginForm1Step(_LoginFormInput, _LoginForm1Step, _LoginFormSharedDefaults):
    """Settings for login form page in 1 step where both username and password are displayed at once.

    url: Optional URL to login page.

    post_login_url: Optionally await redirect to this URL as a user is typically redirected automatically to a new page or view after logging in.

    post_login_element_xpath: Upon successful login, optionally await this element to be loaded."""

    def __init__(self,
                 username_input_xpath: str,
                 password_input_xpath: str,
                 submit_button_xpath: str,
                 url: str | None = None,
                 post_login_wait_seconds: int | None = None,
                 post_login_url: str | None = None,
                 post_login_element_xpath: str | None = None
                 ) -> None:
        _LoginFormInput.__init__(self, username_input_xpath, password_input_xpath)
        _LoginForm1Step.__init__(self, submit_button_xpath)
        _LoginFormSharedDefaults.__init__(self, url, post_login_wait_seconds, post_login_url, post_login_element_xpath)


class LoginForm2Steps(_LoginFormInput, _LoginForm2Steps, _LoginFormSharedDefaults):
    """Settings for login form page in 2 steps where username is prompted first, and once confirmed, then the password can be entered.

    url: Optional URL to login page.

    post_login_url: Optionally await redirect to this URL as a user is typically redirected automatically to a new page or view after logging in.

    post_login_element_xpath: Upon successful login, optionally await this element to be loaded."""

    def __init__(self,
                 username_input_xpath: str,
                 username_submit_button_xpath: str,
                 password_input_xpath: str,
                 password_submit_button_xpath: str,
                 url: str | None = None,
                 post_login_wait_seconds: int | None = None,
                 post_login_url: str | None = None,
                 post_login_element_xpath: str | None = None
                 ) -> None:
        _LoginFormInput.__init__(self, username_input_xpath, password_input_xpath)
        _LoginForm2Steps.__init__(self, username_submit_button_xpath, password_submit_button_xpath)
        _LoginFormSharedDefaults.__init__(self, url, post_login_wait_seconds, post_login_url, post_login_element_xpath)
