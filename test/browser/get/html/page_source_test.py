import _helper
import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize(
    "url", [(internal_url.MINI_SITE_HOMEPAGE), (internal_url.MINI_SITE_FEATURE_1), (internal_url.MINI_SITE_ABOUT)]
)
def test_get_html_page_source(url: str, browser_default_headless: Browser) -> None:
    def normalize_line_endings(text: str) -> str:
        """There's a difference in line endings between the browser and the file system, so we normalize without changing the actual HTML code."""

        split_text = text.splitlines()
        normalized_text = "".join(split_text)
        return normalized_text

    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    loaded_page_source = browser.get.html.page_source()
    loaded_page_source = normalize_line_endings(loaded_page_source)

    url_as_file_path = _helper.url.convert_internal_url_to_file_path(url)
    with open(url_as_file_path) as file:
        expected_page_source = file.read()
    expected_page_source = expected_page_source.replace(
        "<!DOCTYPE html>", "", 1
    )  # Document type isn't part of page source returned by the browser.
    expected_page_source = normalize_line_endings(expected_page_source)

    assert loaded_page_source == expected_page_source
