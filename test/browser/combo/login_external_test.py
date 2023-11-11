from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.log_in import (AMAZON_LOGIN_CREDENTIALS, AMAZON_LOGIN_FORM, JYLLANDSPOSTEN_LOGIN_CREDENTIALS,
                                  JYLLANDSPOSTEN_LOGIN_FORM)
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import external_url

from browserist import Browser, CookieBannerSettings, LoginCredentials, LoginForm1Step, LoginForm2Steps


@pytest.mark.parametrize("url, login_credentials, login_form", [
    (external_url.AMAZON_COM, AMAZON_LOGIN_CREDENTIALS, AMAZON_LOGIN_FORM),
    (external_url.JYLLANDSPOSTEN_DK, JYLLANDSPOSTEN_LOGIN_CREDENTIALS, JYLLANDSPOSTEN_LOGIN_FORM),
])
def test_combo_login_with_1_and_2_steps_external(
    url: str,
    login_credentials: LoginCredentials,
    login_form: LoginForm1Step | LoginForm2Steps,
    browser_default_disable_images: Browser
) -> None:

    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_disable_images)
        browser.open.url(url)
        browser.combo.log_in(login_credentials, login_form)
