from typing import Any

import lxml.etree  # type: ignore
from lxml.etree import XPathSyntaxError

from ..model.type.xpath import XPath


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


def mediate_default_none(value: str | None) -> XPath | None:
    return None if value is None else XPath(value)
