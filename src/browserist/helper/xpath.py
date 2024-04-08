import lxml.etree
from lxml.etree import XPathSyntaxError

from ..model.type.xpath import XPath


def is_valid(xpath: str) -> bool:
    try:
        return bool(lxml.etree.XPath(xpath))
    except (XPathSyntaxError, Exception):
        return False


def mediate_conversion_to_tiny_type_or_none(value: str | None) -> XPath | None:
    """Mediate conversion of string to XPath tiny type or keep None type."""

    return None if value is None else XPath(value)
