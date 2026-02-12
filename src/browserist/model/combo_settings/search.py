from dataclasses import dataclass

from ... import helper
from ...model.type.xpath import XPath


@dataclass(kw_only=True, slots=True)
class SearchSettings:
    """Settings class for the search combo.

    Args:
        url (str | None, optional): URL for the search page. Sometimes not needed if, for example, the search input field is available on all pages.
        input_xpath (str): XPath for the search input field.
        button_xpath (str): XPath for the search button.
        await_search_results_url_contains (str | None, optional): Optionally wait for the search results page URL to change.
        await_search_results_xpath (str | None, optional): Optionally wait for a search result element to be ready.
    """

    url: str | None = None
    input_xpath: str
    button_xpath: str
    await_search_results_url_contains: str | None = None
    await_search_results_xpath: str | None = None

    def __post_init__(self) -> None:
        self.input_xpath = XPath(self.input_xpath)
        self.button_xpath = XPath(self.button_xpath)
        self.url = helper.url.mediate_conversion_to_tiny_type_or_none(self.url)
        self.await_search_results_xpath = helper.xpath.mediate_conversion_to_tiny_type_or_none(
            self.await_search_results_xpath
        )
