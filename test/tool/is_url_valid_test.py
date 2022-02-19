import pytest
from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

@pytest.mark.parametrize("url, expected", [
    ("http://foo.com/blah_blah", True),
    ("http://foo.com/blah_blah/", True),
    ("http://foo.com/blah_blah_(wikipedia)", True),
    ("http://foo.com/blah_blah_(wikipedia)_(again)", True),
    ("http://userid:password@example.com:8080", True),
    ("http://invalid.com/perl.cgi?key=", True),
    ("http://web-site.com/cgi-bin/perl.cgi?key1=value1&key2", True)
])
def test_tool_is_url_valid(url: str, expected: bool) -> None:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        assert browser.tool.is_url_valid(url) is expected
