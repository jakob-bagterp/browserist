from contextlib import nullcontext as expectation_of_no_exceptions_raised
from typing import Any

import pytest
from _config.combo.log_in import (LOGIN_CREDENTIALS_INVALID, LOGIN_CREDENTIALS_INVALID_PASSWORD,
                                  LOGIN_CREDENTIALS_INVALID_USERNAME, LOGIN_CREDENTIALS_VALID, LOGIN_FORM_1_STEP,
                                  LOGIN_FORM_2_STEPS)
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, LoginCredentials
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize("login_credentials, expected_landing_page", [
    (LOGIN_CREDENTIALS_VALID, "homepage.html"),
    (LOGIN_CREDENTIALS_INVALID, "error.html"),
])
def test_combo_log_in_1_step(
    login_credentials: LoginCredentials,
    expected_landing_page: str,
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(internal_url.LOG_IN_1_STEP)
        browser.combo.log_in(login_credentials, LOGIN_FORM_1_STEP)
        landing_page_url = browser.get.url.current()
        assert landing_page_url.endswith(expected_landing_page)


@pytest.mark.parametrize("login_credentials, expected_landing_page, expectation", [
    (LOGIN_CREDENTIALS_VALID, "homepage.html", expectation_of_no_exceptions_raised()),
    (LOGIN_CREDENTIALS_INVALID_USERNAME, "error.html", pytest.raises(WaitForElementTimeoutException)),
    (LOGIN_CREDENTIALS_INVALID_PASSWORD, "error.html", expectation_of_no_exceptions_raised()),
])
def test_combo_log_in_2_steps(
    login_credentials: LoginCredentials,
    expected_landing_page: str,
    expectation: Any,
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation:
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(internal_url.LOG_IN_2_STEPS)
        browser.combo.log_in(login_credentials, LOGIN_FORM_2_STEPS)
        landing_page_url = browser.get.url.current()
        assert landing_page_url.endswith(expected_landing_page)