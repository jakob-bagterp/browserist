from dataclasses import dataclass
from typing import Any

from ... import helper
from ...model.type.xpath import XPath


@dataclass
class CookieBannerSettings:
    """Object with data needed to accept or decline cookies from a banner.

    button_xpath: Can be for either accept or decline cookies.

    url: Optional URL from where to handle the cookie banner.

    has_loaded_wait_seconds: Minor grace time to make sure the cookie banner has loaded.

    has_loaded_xpath: Check if banner element has loaded so the cookie banner is ready.

    has_disappeared_wait_seconds: Minor grace time to make sure the cookie banner has disappeared and that the cookie information has been saved before proceeding."""

    button_xpath: XPath
    url: str | None = None
    has_loaded_wait_seconds: int | None = None
    has_loaded_xpath: XPath | None = None
    has_disappeared_wait_seconds: int | None = None

    def __setattr__(self, name: str, value: Any) -> None:
        self = helper.xpath.set_attributes(self, name, value, ["button_xpath", "has_loaded_xpath"])
