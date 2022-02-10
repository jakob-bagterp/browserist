from dataclasses import dataclass
from typing import Union

@dataclass
class SearchSettings:
    """Object with data needed to accept or decline cookies from a banner.

    term: Which terms to input in the search field.

    input_xpath: XPath for the search input field.

    button_xpath: XPath for the search button.

    url: Optional URL for the search page.

    await_search_results_url: Optional wait for the search results page to load.

    await_search_results_xpath: Optional wait for a search result element to be ready."""

    term: str
    input_xpath: str
    button_xpath: str
    url: Union[str, None] = None
    await_search_results_url: Union[str, None] = None
    await_search_results_xpath: Union[str, None] = None
