from typing import Any

import lxml.etree  # type: ignore
from lxml.etree import XPathSyntaxError

from ..model.type.xpath import XPath


def ensure_encoding_of_single_and_double_quotes(xpath: str) -> str:
    """It's recommended to use only single quotes in XPath expressions. It that for some reason isn't the case, this helper converts double to single quotes and handles edge cases of apostrophes. Other functions, e.g. using JavaScript, may break if single and double quotes aren't reliable."""

    def convert_double_to_single_quotes(xpath: str) -> str:
        return xpath.replace("\"", "\'")

    def convert_double_and_single_quotes_to_literals(xpath: str) -> str:
        return xpath.replace('"', '\"').replace("'", "\'")

    if "\"" in xpath:
        if "\'" in xpath:  # If contains mix of both single and double quotes.
            xpath = convert_double_and_single_quotes_to_literals(xpath)
            # TODO: Handle strings with mixed single and double quotes.
            return xpath
        return convert_double_to_single_quotes(xpath)
    return xpath


def is_valid(xpath: str) -> bool:
    try:
        return bool(lxml.etree.XPath(xpath))
    except (XPathSyntaxError, Exception):
        return False


def set_attributes(self: Any, name: str, value: Any, attributes: list[str]) -> Any:
    """Intended for the __setattr__ dunder method in data classes where some string arguments need to be validated and set as XPath.

    Note that this is only supported for data classes when __dict__ is used and not __slots__."""

    if name and value:
        self.__dict__[name] = XPath(value) if name in attributes else value
    return self


def mediate_conversion_to_tiny_type_or_none(value: str | None) -> XPath | None:
    """Mediate conversion of string to XPath tiny type or keep None type."""

    return None if value is None else XPath(value)
