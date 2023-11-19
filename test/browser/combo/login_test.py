import pytest
from _config.combo.log_in import LOGIN_CREDENTIALS_INVALID, LOGIN_CREDENTIALS_VALID, LOGIN_FORM_1_STEP
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, LoginCredentials


@pytest.mark.parametrize("login_credentials, expected_landing_page", [
    (LOGIN_CREDENTIALS_VALID, "homepage.html"),
    (LOGIN_CREDENTIALS_INVALID, "error.html"),
])
def test_combo_login_with_1_step(
    login_credentials: LoginCredentials,
    expected_landing_page: str,
    browser_default_headless_disable_images: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_disable_images)
    browser.open.url(internal_url.LOG_IN_1_STEP)
    browser.combo.log_in(login_credentials, LOGIN_FORM_1_STEP)
    landing_page_url = browser.get.url.current()
    assert landing_page_url.endswith(expected_landing_page)
