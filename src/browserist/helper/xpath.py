import lxml.etree  # type: ignore
from lxml.etree import XPathSyntaxError


def is_valid(xpath: str) -> bool:
    try:
        return bool(lxml.etree.XPath(xpath))
    except (XPathSyntaxError, Exception):
        return False
