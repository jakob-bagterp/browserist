from dataclasses import dataclass

from ... import helper
from ...model.type.xpath import XPath


@dataclass(kw_only=True, slots=True)
class CookieBannerSettings:
    """Object with data needed to accept or decline cookies from a banner.

    button_xpath: Can be for either accept or decline cookies.

    url: Optional URL from where to handle the cookie banner.

    has_loaded_wait_seconds: Minor grace time to make sure the cookie banner has loaded.

    has_loaded_xpath: Check if banner element has loaded so the cookie banner is ready.

    has_disappeared_wait_seconds: Minor grace time to make sure the cookie banner has disappeared and that the cookie information has been saved before proceeding."""

    button_xpath: str
    url: str | None = None
    has_loaded_wait_seconds: int | None = None
    has_loaded_xpath: str | None = None
    has_disappeared_wait_seconds: int | None = None

    def __post_init__(self) -> None:
        self.button_xpath = XPath(self.button_xpath)
        self.has_loaded_xpath = helper.xpath.mediate_default_none(self.has_loaded_xpath)
