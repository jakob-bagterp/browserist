from dataclasses import dataclass

from ... import helper
from ...model.type.xpath import XPath


@dataclass(kw_only=True, slots=True)
class LoginForm1Step:
    """Settings for login form page in 1 step where both username and password are displayed at once.

    Args:
        url (str | None, optional): URL to login page.
        username_input_xpath (str): XPath for username input field.
        password_input_xpath (str): XPath for password input field.
        submit_button_xpath (str): XPath for submit button.
        post_login_wait_seconds (float | None, optional): Minor grace time to ensure the login has completed.
        post_login_url_contains (str | None, optional): Optionally await redirect to this URL as a user is typically redirected automatically to a new page or view after logging in.
        post_login_element_xpath (str | None, optional): Upon successful login, optionally await this element to be loaded.
    """

    username_input_xpath: str
    password_input_xpath: str
    submit_button_xpath: str  # Specific for this class.

    # Shared defaults:
    url: str | None = None
    post_login_wait_seconds: float | None = None
    post_login_url_contains: str | None = None
    post_login_element_xpath: str | None = None

    def __post_init__(self) -> None:
        self.username_input_xpath = XPath(self.username_input_xpath)
        self.password_input_xpath = XPath(self.password_input_xpath)
        self.submit_button_xpath = XPath(self.submit_button_xpath)
        self.url = helper.url.mediate_conversion_to_tiny_type_or_none(self.url)
        self.post_login_element_xpath = helper.xpath.mediate_conversion_to_tiny_type_or_none(
            self.post_login_element_xpath)


@dataclass(kw_only=True, slots=True)
class LoginForm2Steps:
    """Settings for login form page in 2 steps where username is prompted first, and once confirmed, then the password can be entered.

    Args:
        url (str | None, optional): URL to login page.
        username_input_xpath (str): XPath for username input field.
        username_submit_button_xpath (str): XPath for username submit button.
        password_input_xpath (str): XPath for password input field.
        password_submit_button_xpath (str): XPath for password submit button.
        post_login_wait_seconds (float | None, optional): Minor grace time to ensure the login has completed.
        post_login_url_contains (str | None, optional): Optionally await redirect to this URL as a user is typically redirected automatically to a new page or view after logging in.
        post_login_element_xpath (str | None, optional): Upon successful login, optionally await this element to be loaded.
    """

    username_input_xpath: str
    username_submit_button_xpath: str  # Specific for this class.
    password_input_xpath: str
    password_submit_button_xpath: str  # Specific for this class.

    # Shared defaults:
    url: str | None = None
    post_login_wait_seconds: float | None = None
    post_login_url_contains: str | None = None
    post_login_element_xpath: str | None = None

    def __post_init__(self) -> None:
        self.username_input_xpath = XPath(self.username_input_xpath)
        self.username_submit_button_xpath = XPath(self.username_submit_button_xpath)
        self.password_input_xpath = XPath(self.password_input_xpath)
        self.password_submit_button_xpath = XPath(self.password_submit_button_xpath)
        self.url = helper.url.mediate_conversion_to_tiny_type_or_none(self.url)
        self.post_login_element_xpath = helper.xpath.mediate_conversion_to_tiny_type_or_none(
            self.post_login_element_xpath)
