import time
from contextlib import nullcontext as expectation_of_no_exceptions_raised
from typing import Any

import _helper
import pytest
from _config.combo.log_in import (
    ERROR_LANDING_PAGE,
    LOGIN_CREDENTIALS_INVALID,
    LOGIN_CREDENTIALS_INVALID_PASSWORD,
    LOGIN_CREDENTIALS_INVALID_USERNAME,
    LOGIN_CREDENTIALS_VALID,
    LOGIN_FORM_1_STEP,
    LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES,
    LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT,
    LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_URL,
    LOGIN_FORM_2_STEPS,
    LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES,
    LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT,
    LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_URL,
    SUCCESS_LANDING_PAGE,
)
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, LoginCredentials, LoginForm1Step, LoginForm2Steps
from browserist.exception.timeout import WaitForElementTimeoutException


@pytest.mark.parametrize(
    "login_credentials, expected_landing_page",
    [(LOGIN_CREDENTIALS_VALID, SUCCESS_LANDING_PAGE), (LOGIN_CREDENTIALS_INVALID, ERROR_LANDING_PAGE)],
)
@pytest.mark.xdist_group(name="serial_combo_log_in_tests")
def test_combo_log_in_1_step(
    login_credentials: LoginCredentials, expected_landing_page: str, browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(internal_url.LOG_IN_1_STEP)
        LOGIN_FORM_1_STEP.post_login_url_contains = expected_landing_page
        browser.combo.log_in(login_credentials, LOGIN_FORM_1_STEP)
        landing_page_url = browser.get.url.current()
        assert landing_page_url.endswith(expected_landing_page)


@pytest.mark.parametrize(
    "login_credentials, expected_landing_page, expectation",
    [
        (LOGIN_CREDENTIALS_VALID, SUCCESS_LANDING_PAGE, expectation_of_no_exceptions_raised()),
        (LOGIN_CREDENTIALS_INVALID_USERNAME, ERROR_LANDING_PAGE, pytest.raises(WaitForElementTimeoutException)),
        (LOGIN_CREDENTIALS_INVALID_PASSWORD, ERROR_LANDING_PAGE, expectation_of_no_exceptions_raised()),
    ],
)
@pytest.mark.xdist_group(name="serial_combo_log_in_tests")
def test_combo_log_in_2_steps(
    login_credentials: LoginCredentials,
    expected_landing_page: str,
    expectation: Any,
    browser_default_headless_disable_images: Browser,
) -> None:
    with expectation:
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(internal_url.LOG_IN_2_STEPS)
        LOGIN_FORM_2_STEPS.post_login_url_contains = expected_landing_page
        browser.combo.log_in(login_credentials, LOGIN_FORM_2_STEPS)
        landing_page_url = browser.get.url.current()
        assert landing_page_url.endswith(expected_landing_page)


@pytest.mark.parametrize(
    "url, login_form",
    [(internal_url.LOG_IN_1_STEP, LOGIN_FORM_1_STEP), (internal_url.LOG_IN_2_STEPS, LOGIN_FORM_2_STEPS)],
)
@pytest.mark.xdist_group(name="serial_combo_log_in_tests")
def test_combo_log_in_post_login_wait_seconds(
    url: str, login_form: LoginForm1Step | LoginForm2Steps, browser_default_headless_disable_images: Browser
) -> None:
    def log_in_and_get_time(
        browser: Browser, url: str, login_form: LoginForm1Step | LoginForm2Steps, post_login_wait_seconds: float
    ) -> float:
        browser.open.url(url)
        login_form.post_login_wait_seconds = post_login_wait_seconds
        start_time = time.perf_counter()
        browser.combo.log_in(LOGIN_CREDENTIALS_VALID, login_form)
        stop_time = time.perf_counter()
        return _helper.time.get_difference(start_time, stop_time)

    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        login_form.post_login_url_contains = SUCCESS_LANDING_PAGE  # Reset to default value due to earlier tests.
        post_login_wait_seconds_a = 1
        post_login_wait_seconds_b = post_login_wait_seconds_a + 1
        time_measured_a = log_in_and_get_time(browser, url, login_form, post_login_wait_seconds_a)
        time_measured_b = log_in_and_get_time(browser, url, login_form, post_login_wait_seconds_b)
        assert time_measured_a < time_measured_b
        time_difference_a_b = _helper.time.get_difference(post_login_wait_seconds_a, post_login_wait_seconds_b)
        time_difference_measured_a_b = _helper.time.get_difference(time_measured_a, time_measured_b)
        assert time_difference_measured_a_b >= _helper.tolerance.deduct(time_difference_a_b, 20)


@pytest.mark.parametrize(
    "login_form, login_credentials, expected_state",
    [
        (LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES, LOGIN_CREDENTIALS_VALID, True),
        (LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_URL, LOGIN_CREDENTIALS_VALID, True),
        (LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT, LOGIN_CREDENTIALS_VALID, True),
        (LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES, LOGIN_CREDENTIALS_INVALID_PASSWORD, False),
        (LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES, LOGIN_CREDENTIALS_VALID, True),
        (LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_URL, LOGIN_CREDENTIALS_VALID, True),
        (LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT, LOGIN_CREDENTIALS_VALID, True),
        (LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES, LOGIN_CREDENTIALS_INVALID_PASSWORD, False),
    ],
)
@pytest.mark.xdist_group(name="serial_combo_log_in_tests")
def test_combo_log_in_state(
    login_form: LoginForm1Step | LoginForm2Steps,
    login_credentials: LoginCredentials,
    expected_state: bool,
    browser_default_headless_disable_images: Browser,
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_disable_images)
    state = browser.combo.log_in(login_credentials, login_form)
    assert state is expected_state
