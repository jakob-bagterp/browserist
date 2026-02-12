import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url, xpath, expected_width, expected_height",
    [
        (
            internal_url.MINI_SITE_HOMEPAGE,
            "//section[@class='hero hero__background-image__office-ideas-on-board']",
            1008,
            400,
        ),
        (internal_url.MINI_SITE_HOMEPAGE, "//div[@class='hero__text-box']", 340, 160),
        (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/p[1]", 600, 185),
        (internal_url.MINI_SITE_FEATURE_1, "//*[@id='main']/img", 600, 400),
    ],
)
def test_get_dimensions(
    url: str, xpath: str, expected_width: int, expected_height: int, browser_default_headless_fixed_viewport: Browser
) -> None:
    browser = reset_to_not_timed_out(browser_default_headless_fixed_viewport)
    browser.open.url(url)
    measured_width, measured_height = browser.get.dimensions(xpath)
    assert expected_width == measured_width
    assert expected_height == measured_height
