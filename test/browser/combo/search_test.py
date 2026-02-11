from contextlib import nullcontext as expectation_of_no_exceptions_raised

import pytest
from _config.combo.search import SEARCH_SETTINGS
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

SEARCH_RESULTS_XPATH = "//*[@id='search-results']/div[@class='search-result-item']"


@pytest.mark.parametrize("term, expected_result_elements, expected_first_result_starts_with", [
    ("fruits", 7, "Apple"),
    ("no results", 1, "No results found"),
])
@pytest.mark.xdist_group(name="serial_combo_search_tests")
def test_combo_search(
    term: str,
    expected_result_elements: int,
    expected_first_result_starts_with: str,
    browser_default_headless_disable_images: Browser
) -> None:
    with expectation_of_no_exceptions_raised():
        browser = reset_to_not_timed_out(browser_default_headless_disable_images)
        browser.open.url(internal_url.SEARCH)
        browser.combo.search(term, SEARCH_SETTINGS)
        result_elements = browser.tool.count_elements(SEARCH_RESULTS_XPATH)
        assert result_elements == expected_result_elements
        first_result_text = browser.get.text(f"{SEARCH_RESULTS_XPATH}[1]")
        assert first_result_text.startswith(expected_first_result_starts_with)
