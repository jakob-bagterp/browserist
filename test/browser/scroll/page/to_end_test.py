import pytest
from _helper.python import is_python_version
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser
from browserist.helper import operating_system


@pytest.mark.xdist_group(name="serial_scroll_tests")
def test_scroll_to_end_of_page(browser_default_headless: Browser) -> None:
    # TODO: Remove this once we have a fix for this exception:
    if operating_system.is_macos() and any(
        [is_python_version(3, 11), is_python_version(3, 12), is_python_version(3, 13), is_python_version(3, 14)]
    ):
        pytest.skip(
            "When this runs on MacOS with Python 3.11, 3.12, 3.13 or 3.14, the last scroll position assertion fails."
        )

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.SCROLL_LONG_VERTICAL)
    total_srcroll_height = browser.scroll.get.total_height()
    assert total_srcroll_height > 0
    browser.scroll.page.to_top()
    x_default, y_default = browser.scroll.get.position()
    assert x_default == 0
    assert y_default == 0
    browser.scroll.page.to_end()
    x_end, y_end = browser.scroll.get.position()
    assert x_end == 0
    assert y_end > y_default
