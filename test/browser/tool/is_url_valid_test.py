import pytest
from _helper import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, expected", [
    ("http://www.example.com", True),
    ("https://www.example.com", True),
    ("http://blog.example.com", True),
    ("http://www.example.com/product", True),
    ("http://www.example.com/products?id=1&page=2", True),
    ("http://www.example.com#up", True),
    ("http://255.255.255.255", True),
    ("http://invalid.com/perl.cgi?key=", True),
    ("http://web-site.com/cgi-bin/perl.cgi?key1=value1&key2", True),
    ("http://www.site.com:8008", True),
    ("http://userid:password@example.com:8080", True),

    ("example.com", False),
    ("www.example.com", False),
    ("https:/www.example.com", False),
    ("255.255.255.255", False),

    ("http://foo.com/blah_blah", True),
    ("http://foo.com/blah_blah/", True),
    ("http://foo.com/blah_blah_(wikipedia)", True),
    ("http://foo.com/blah_blah_(wikipedia)_(again)", True),
    ("http://userid:password@example.com:8080", True)
])
def test_tool_is_url_valid(url: str, expected: bool, browser_default_headless: Browser) -> None:
    """References for URL regex pattern and other methods of validating URLs:

    https://www.regextester.com/94502

    https://mathiasbynens.be/demo/url-regex

    https://stackoverflow.com/a/52455972/13115170"""

    browser = browser_default_headless
    browser.open.url_if_not_current(internal_url.EXAMPLE_COM)
    assert browser.tool.is_url_valid(url) is expected
