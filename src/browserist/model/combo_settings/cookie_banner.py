from dataclasses import dataclass

from ... import helper
from ...model.type.xpath import XPath


@dataclass(kw_only=True, slots=True)
class CookieBannerSettings:
    """Object with data needed to accept or decline cookies from a banner.

    Args:
        url (str | None, optional): URL from where to handle the cookie banner.
        iframe_xpath (str | None, optional): Use if the cookie banner is inside an iframe. If used, all other XPath elements are relative to this iframe.
        has_loaded_wait_seconds (float | None, optional): Minor grace time to ensure the cookie banner has loaded. Often due an fade-in animation or similar transition.
        has_loaded_xpath (str | None, optional): Check if cookie banner has loaded so it's ready for interaction.
        button_xpath (str): Can be for either accept or decline cookies.
        has_disappeared_wait_seconds (float | None, optional): Minor grace time to ensure the cookie banner has disappeared – often due an animation – and that the cookie information has been saved before proceeding.
    """

    url: str | None = None
    iframe_xpath: str | None = None
    has_loaded_wait_seconds: float | None = None
    has_loaded_xpath: str | None = None
    button_xpath: str
    has_disappeared_wait_seconds: float | None = None

    def __post_init__(self) -> None:
        self.url = helper.url.mediate_conversion_to_tiny_type_or_none(self.url)
        self.iframe_xpath = helper.xpath.mediate_conversion_to_tiny_type_or_none(self.iframe_xpath)
        self.has_loaded_xpath = helper.xpath.mediate_conversion_to_tiny_type_or_none(self.has_loaded_xpath)
        self.button_xpath = XPath(self.button_xpath)
