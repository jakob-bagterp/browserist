from dataclasses import dataclass


@dataclass
class LoginCredentials:
    """Object to define a user profile's access credentials.

    Separated from the login form so that the multiple users/roles can use the same form."""

    username: str
    password: str


@dataclass
class LoginForm1Step:
    """Settings for login form page in 1 step where both username and password are displayed at once.

    url: Optional URL to login page.

    post_login_url: Optionally await redirect to this URL as a user is typically redirected automatically to a new page or view after logging in.

    post_login_element_xpath: Upon successful login, optionally await this element to be loaded."""

    username_input_xpath: str
    password_input_xpath: str
    submit_button_xpath: str
    url: str | None = None
    post_login_wait_seconds: int | None = None
    post_login_url: str | None = None
    post_login_element_xpath: str | None = None


@dataclass
class LoginForm2Steps:
    """Settings for login form page in 2 steps where username is prompted first, and once confirmed, then the password can be entered.

    url: Optional URL to login page.

    post_login_url: Optionally await redirect to this URL as a user is typically redirected automatically to a new page or view after logging in.

    post_login_element_xpath: Upon successful login, optionally await this element to be loaded."""

    username_input_xpath: str
    username_submit_button_xpath: str
    password_input_xpath: str
    password_submit_button_xpath: str
    url: str | None = None
    post_login_wait_seconds: int | None = None
    post_login_url: str | None = None
    post_login_element_xpath: str | None = None
