from typing import Any

import lxml.etree  # type: ignore
from lxml.etree import XPathSyntaxError

from ..constant.char import DOUBLE_QUOTE, QUOTES, SINGLE_QUOTE
from ..model.type.xpath import XPath


def ensure_encoding_of_single_and_double_quotes(xpath: str) -> str:
    """It's recommended to use only single quotes in XPath expressions. It that for some reason isn't the case, this helper converts double to single quotes and handles edge cases of apostrophes. Other functions, e.g. using JavaScript, may break if single and double quotes aren't reliable."""

    def convert_double_to_single_quotes(xpath: str) -> str:
        """Disclaimer: Should be used with care and only when a string doesn't have single quotes. Otherwise and if used on mix of single and double quotes, it may lead to syntax issue."""

        return xpath.replace(DOUBLE_QUOTE, SINGLE_QUOTE)

    def convert_string_of_double_and_single_quotes_to_concat(xpath: str) -> str:
        """Example: Converts "Fred's \"Fancy Pizza\"" to "concat('Fred', "'", 's "Fancy Pizza"')"""""

        return "concat('" + xpath.replace("'", "', \"'\" ,'") + "')"

    if any(quote in xpath for quote in QUOTES):
        if DOUBLE_QUOTE not in xpath:
            return xpath
        if SINGLE_QUOTE not in xpath:
            return convert_double_to_single_quotes(xpath)
        else:  # If contains mix of both single and double quotes.
            # TODO: Handle strings with mixed single and double quotes.
            return xpath
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
