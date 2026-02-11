from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.exception.scroll import PageValueError


@pytest.mark.parametrize("pages", [
    1,
    2,
    3,
    4,
    5,
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_page_down(pages: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    browser.scroll.page.to_top()
    _, y_top = browser.scroll.get.position()
    y_screen_height = browser.viewport.get.height()
    browser.scroll.page.down(pages)
    _, y_page_down = browser.scroll.get.position()
    assert y_page_down == y_top + (y_screen_height + 1) * pages


@pytest.mark.parametrize("pages, expectation", [
    (1, does_not_raise()),
    (3, does_not_raise()),
    (0, pytest.raises(PageValueError)),
    (-1, pytest.raises(PageValueError)),
    ("2", pytest.raises(PageValueError)),
    (3.14, pytest.raises(PageValueError)),
])
@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_page_down_exceptions(pages: int, expectation: Any, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    with expectation:
        browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
        browser.scroll.page.down(pages)
