from _helper.url import external_url

from browserist import SearchSettings

DBA_SEARCH = SearchSettings(
    input_xpath="//input[@id='searchField']",
    button_xpath="//form//button[contains(@class, 'btn-search')]",
    url=external_url.DBA_DK,
    await_search_results_url_contains=f"{external_url.DBA_DK}soeg/?soeg=",
    await_search_results_xpath="//input[@id='searchField']"
)

GOOGLE_SEARCH = SearchSettings(
    input_xpath="//div/input[1]",
    button_xpath="(//input[@name='btnK'])[2]",
    url=external_url.GOOGLE_COM,
    await_search_results_url_contains=f"{external_url.GOOGLE_COM}search?"
)
