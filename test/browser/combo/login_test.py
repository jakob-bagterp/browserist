from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.log_in import AMAZON_LOGIN_CREDENTIALS, AMAZON_LOGIN_FORM
from _helper import external_url

from browserist import Browser, CookieBannerSettings, LoginCredentials, LoginForm1Step, LoginForm2Steps


@pytest.mark.parametrize("url, login_credentials, login_form, cookie_banner_settings", [
    (external_url.AMAZON_COM, AMAZON_LOGIN_CREDENTIALS, AMAZON_LOGIN_FORM, None),
])
def test_combo_login_with_1_and_2_steps(
    url: str,
    login_credentials: LoginCredentials,
    login_form: LoginForm1Step | LoginForm2Steps,
    cookie_banner_settings: CookieBannerSettings | None,
    browser_default_disable_images: Browser
) -> None:

    with expectation_of_no_exceptions_raised():
        browser = browser_default_disable_images
        browser.open.url(url)
        if cookie_banner_settings:
            browser.combo.cookie_banner(cookie_banner_settings)
        browser.combo.log_in(login_credentials, login_form)
