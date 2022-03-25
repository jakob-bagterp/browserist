import lxml.etree  # type: ignore
from lxml.etree import XPathSyntaxError as LXML_XPathSyntaxError

from ..exception.xpath import XPathSyntaxError


def is_valid(xpath: str) -> bool:
    try:
        return bool(lxml.etree.XPath(xpath))
    except LXML_XPathSyntaxError:
        raise XPathSyntaxError(xpath) from LXML_XPathSyntaxError(xpath)
    except Exception:
        raise XPathSyntaxError(xpath) from Exception
