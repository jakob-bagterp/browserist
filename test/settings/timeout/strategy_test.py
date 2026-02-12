from typing import Any

import pytest
from _config.timeout_strategy import BrowserCallable
from _helper.timeout import (
    reset_to_not_timed_out,
    set_timeout_strategy_to_continue,
    set_timeout_strategy_to_stop,
    set_to_timed_out,
)
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.mini_site.feature_1 import (
    MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH,
    MINI_SITE_FEATURE_1_IMAGE_1_XPATH,
)

from browserist import Browser, BrowserSettings, TimeoutSettings

browser_settings = BrowserSettings(
    headless=True, disable_images=True, timeout=TimeoutSettings(seconds=1), check_connection=False
)

browser = Browser(browser_settings)

METHODS_WITH_RETURN_VALUES: list[tuple[Browser, Any, list[str]]] = [
    (browser, browser.check_if.contains_any_text, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.check_if.contains_text, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH, "Feature 1"]),
    (browser, browser.check_if.does_exist, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.check_if.is_clickable, ["/html/body/header/nav/ul/li[1]/a"]),
    (browser, browser.check_if.is_disabled, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.check_if.is_displayed, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.check_if.is_enabled, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.check_if.is_image_loaded, [MINI_SITE_FEATURE_1_IMAGE_1_XPATH]),
    (browser, browser.check_if.is_selected, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.get.attribute.value, ["/html/body/header/nav/ul/li[1]/a", "href"]),
    (browser, browser.get.attribute.values, ["//a", "href"]),
    (browser, browser.get.dimensions, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.get.element, ["//*[@id='main']/p[1]"]),
    (browser, browser.get.elements, ["//p"]),
    (browser, browser.get.elements_by_tag, ["p"]),
    (browser, browser.get.html.element_inner, ["//body"]),
    (browser, browser.get.html.element_outer, ["//body"]),
    (browser, browser.get.html.page_source, []),
    (browser, browser.get.page_title, []),
    (browser, browser.get.text, [MINI_SITE_FEATURE_1_HEADLINE_H1_XPATH]),
    (browser, browser.get.texts, ["//h2"]),
    (browser, browser.get.url.current, []),
    (browser, browser.get.url.from_image, [MINI_SITE_FEATURE_1_IMAGE_1_XPATH]),
    (browser, browser.get.url.from_images, ["//img"]),
    (browser, browser.get.url.from_link, ["/html/body/header/nav/ul/li[1]/a"]),
    (browser, browser.get.url.from_links, ["//a"]),
    (browser, browser.scroll.check_if.is_end_of_page, []),
    (browser, browser.scroll.check_if.is_top_of_page, []),
    (browser, browser.scroll.get.position, []),
    (browser, browser.scroll.get.total_height, []),
    (browser, browser.tool.is_input_valid, [does_not_exist.TEXT, does_not_exist.TEXT]),
    (browser, browser.tool.is_url_valid, [does_not_exist.URL]),
    (browser, browser.tool.count_elements, ["//h2"]),
    (browser, browser.viewport.get.height, []),
    (browser, browser.viewport.get.size, []),
    (browser, browser.viewport.get.width, []),
    (browser, browser.window.get.height, []),
    (browser, browser.window.get.position, []),
    (browser, browser.window.get.size, []),
    (browser, browser.window.get.width, []),
    (browser, browser.window.handle.all, []),
    (browser, browser.window.handle.count, []),
    (browser, browser.window.handle.current, []),
]


@pytest.mark.parametrize("browser, browser_function, args", METHODS_WITH_RETURN_VALUES)
@pytest.mark.xdist_group(name="serial_timeout_strategy_tests")
def test_timeout_strategy_stop(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values are skipped when the timeout is set to stop."""

    browser = set_timeout_strategy_to_stop(browser)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    browser = set_to_timed_out(browser)
    assert browser_function(*args) is None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None


@pytest.mark.parametrize("browser, browser_function, args", METHODS_WITH_RETURN_VALUES)
@pytest.mark.xdist_group(name="serial_timeout_strategy_tests")
def test_timeout_strategy_continue(browser: Browser, browser_function: BrowserCallable, args: Any) -> None:
    """Ensure that methods with return values aren't skipped when the timeout is set to continue."""

    browser = set_timeout_strategy_to_continue(browser)
    browser.open.url(internal_url.MINI_SITE_FEATURE_1)
    browser = set_to_timed_out(browser)
    assert browser_function(*args) is not None
    browser = reset_to_not_timed_out(browser)
    assert browser_function(*args) is not None
