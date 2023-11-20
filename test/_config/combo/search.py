from _mock_data.url import internal_url

from browserist import SearchSettings

SEARCH_SETTINGS = SearchSettings(
    input_xpath="//*[@id='search-input']",
    button_xpath="//*[@id='submit']",
    url=internal_url.SEARCH,
)
