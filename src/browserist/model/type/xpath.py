from ... import helper
from ...exception.xpath import XPathSyntaxError


class XPath:
    """Class to handle and validate XPath input as "tiny type"."""

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
