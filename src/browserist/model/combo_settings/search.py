from dataclasses import dataclass


@dataclass
class SearchSettings:
    """Object with data needed to accept or decline cookies from a banner.

    input_xpath: XPath for the search input field.

    button_xpath: XPath for the search button.

    url: Optional URL for the search page.

    await_search_results_url: Optional wait for the search results page to load.

    await_search_results_xpath: Optional wait for a search result element to be ready."""

    input_xpath: str
    button_xpath: str
    url: str | None = None
    await_search_results_url: str | None = None
    await_search_results_xpath: str | None = None
