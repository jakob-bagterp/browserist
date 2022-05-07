from __future__ import annotations

from ... import helper
from ...exception.xpath import XPathSyntaxError


class XPath(str):
    """Class to handle and validate XPath input as "tiny type"."""

    __slots__ = ["value"]

    def __new__(cls, xpath: str | XPath) -> XPath:
        # If input already is a validated XPath element, bypass and don't create a new object:
        return xpath if isinstance(xpath, XPath) else super().__new__(cls, xpath)

    def __init__(self, xpath: str) -> None:
        if not helper.xpath.is_valid(xpath):
            raise XPathSyntaxError(xpath)
        self.value: str = xpath

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    def is_valid(self) -> bool:
        return helper.xpath.is_valid(self.value)
