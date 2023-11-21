from _mock_data.url import internal_url

from browserist import SearchSettings

SEARCH_SETTINGS = SearchSettings(
    url=internal_url.SEARCH,
    input_xpath="//*[@id='search-input']",
    button_xpath="//*[@id='submit']",
    await_search_results_xpath="//*[@id='search-results']/div[@class='search-result-item']",
)
