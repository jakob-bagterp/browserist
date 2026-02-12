import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_count",
    [
        (internal_url.MINI_SITE_HOMEPAGE, "/html/body/section[2]/div/h3", 3),
        (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/p", 6),
        (internal_url.MINI_SITE_FEATURE_1, "//h2", 2),
        (internal_url.MINI_SITE_FEATURE_1, "//img", 1),
    ],
)
def test_tool_count_elements(url: str, xpath: str, expected_count: int, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.tool.count_elements(xpath) == expected_count
