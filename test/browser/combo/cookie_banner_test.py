import time
from contextlib import nullcontext as expectation_of_no_exceptions_raised

import _helper
import pytest
from _config.combo.cookie_banner import (COOKIE_BANNER_SETTINGS_WITH_IFRAME,
                                         COOKIE_BANNER_SETTINGS_WITH_IFRAME_WITH_RETURN_BOOL_AND_ERROR_STATE,
                                         COOKIE_BANNER_SETTINGS_WITH_IFRAME_WITH_RETURN_BOOL_AND_SUCCESS_STATE,
                                         COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME,
                                         COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME_WITH_RETURN_BOOL_AND_ERROR_STATE,
                                         COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME_WITH_RETURN_BOOL_AND_SUCCESS_STATE)
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser, CookieBannerSettings


@pytest.mark.parametrize("cookie_banner_settings", [
    (COOKIE_BANNER_SETTINGS_WITH_IFRAME),
    (COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME),
])
@pytest.mark.xdist_group(name="serial_combo_cookie_banner_tests")
def test_combo_cookie_banner(
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.combo.cookie_banner(cookie_banner_settings)


PAGE_HEADER_TEXT = "Welcome to the Cookie Banner Test Website"

PAGE_HEADER_XPATH = "/html/body/main/h1"


@pytest.mark.xdist_group(name="serial_combo_cookie_banner_tests")
def test_combo_cookie_banner_return_iframe_to_origin(
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(internal_url.COOKIE_BANNER_WITH_IFRAME)
        assert PAGE_HEADER_TEXT == browser.get.text(PAGE_HEADER_XPATH)
        browser.combo.cookie_banner(COOKIE_BANNER_SETTINGS_WITH_IFRAME)
        assert PAGE_HEADER_TEXT == browser.get.text(PAGE_HEADER_XPATH)


@pytest.mark.parametrize("cookie_banner_settings", [
    (COOKIE_BANNER_SETTINGS_WITH_IFRAME),
    (COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME),
])
@pytest.mark.xdist_group(name="serial_combo_cookie_banner_tests")
def test_combo_cookie_banner_has_loaded_wait_seconds(
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_disable_images: Browser
) -> None:
    def accept_cookie_banner_and_get_time(browser: Browser, cookie_banner_settings: CookieBannerSettings, has_loaded_wait_seconds: float) -> float:
        cookie_banner_settings.has_loaded_wait_seconds = has_loaded_wait_seconds
        start_time = time.perf_counter()
        browser.combo.cookie_banner(cookie_banner_settings)
        stop_time = time.perf_counter()
        return _helper.time.get_difference(start_time, stop_time)

    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        has_loaded_wait_seconds_a = 1
        has_loaded_wait_seconds_b = has_loaded_wait_seconds_a + 1
        time_measured_a = accept_cookie_banner_and_get_time(browser, cookie_banner_settings, has_loaded_wait_seconds_a)
        time_measured_b = accept_cookie_banner_and_get_time(browser, cookie_banner_settings, has_loaded_wait_seconds_b)
        assert time_measured_a < time_measured_b
        time_difference_a_b = _helper.time.get_difference(has_loaded_wait_seconds_a, has_loaded_wait_seconds_b)
        time_difference_measured_a_b = _helper.time.get_difference(time_measured_a, time_measured_b)
        assert time_difference_measured_a_b >= _helper.tolerance.deduct(time_difference_a_b, 30)


@pytest.mark.parametrize("cookie_banner_settings", [
    (COOKIE_BANNER_SETTINGS_WITH_IFRAME),
    (COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME),
])
@pytest.mark.xdist_group(name="serial_combo_cookie_banner_tests")
def test_combo_cookie_banner_has_disappeared_wait_seconds(
    cookie_banner_settings: CookieBannerSettings,
    browser_default_headless_disable_images: Browser
) -> None:
    def accept_cookie_banner_and_get_time(browser: Browser, cookie_banner_settings: CookieBannerSettings, has_disappeared_wait_seconds: float) -> float:
        cookie_banner_settings.has_disappeared_wait_seconds = has_disappeared_wait_seconds
        start_time = time.perf_counter()
        browser.combo.cookie_banner(cookie_banner_settings)
        stop_time = time.perf_counter()
        return _helper.time.get_difference(start_time, stop_time)

    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        has_disappeared_wait_seconds_a = 1
        has_disappeared_wait_seconds_b = has_disappeared_wait_seconds_a + 1
        time_measured_a = accept_cookie_banner_and_get_time(browser, cookie_banner_settings, has_disappeared_wait_seconds_a)
        time_measured_b = accept_cookie_banner_and_get_time(browser, cookie_banner_settings, has_disappeared_wait_seconds_b)
        assert time_measured_a < time_measured_b
        time_difference_a_b = _helper.time.get_difference(has_disappeared_wait_seconds_a, has_disappeared_wait_seconds_b)
        time_difference_measured_a_b = _helper.time.get_difference(time_measured_a, time_measured_b)
        assert time_difference_measured_a_b >= _helper.tolerance.deduct(time_difference_a_b, 30)


@pytest.mark.parametrize("cookie_banner_settings, expected_state", [
    (COOKIE_BANNER_SETTINGS_WITH_IFRAME_WITH_RETURN_BOOL_AND_SUCCESS_STATE, True),
    (COOKIE_BANNER_SETTINGS_WITH_IFRAME_WITH_RETURN_BOOL_AND_ERROR_STATE, False),
    (COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME_WITH_RETURN_BOOL_AND_SUCCESS_STATE, True),
    (COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME_WITH_RETURN_BOOL_AND_ERROR_STATE, False),
])
@pytest.mark.xdist_group(name="serial_combo_cookie_banner_tests")
def test_combo_cookie_banner_state(
    cookie_banner_settings: CookieBannerSettings,
    expected_state: bool,
    browser_default_headless_disable_images: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_disable_images)
    state = browser.combo.cookie_banner(cookie_banner_settings)
    assert state is expected_state
