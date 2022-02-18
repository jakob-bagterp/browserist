from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

def with_browser_tool_is_url_valid(url: str) -> bool:
    with Browser(default.HEADLESS) as browser:
        browser.open.url(internal_url.EXAMPLE_COM)
        return browser.tool.is_url_valid(url)

class TestToolIsUrlValid():
    def test_tool_is_url_valid_1(self) -> None:
        with_browser_tool_is_url_valid("http://foo.com/blah_blah") is True

    def test_tool_is_url_valid_2(self) -> None:
        with_browser_tool_is_url_valid("http://foo.com/blah_blah/") is True

    def test_tool_is_url_valid_3(self) -> None:
        with_browser_tool_is_url_valid("http://foo.com/blah_blah_(wikipedia)") is True

    def test_tool_is_url_valid_4(self) -> None:
        with_browser_tool_is_url_valid("http://foo.com/blah_blah_(wikipedia)_(again)") is True

    def test_tool_is_url_valid_5(self) -> None:
        with_browser_tool_is_url_valid("http://userid:password@example.com:8080") is True

    def test_tool_is_url_valid_6(self) -> None:
        with_browser_tool_is_url_valid("http://invalid.com/perl.cgi?key=") is False

    def test_tool_is_url_valid_7(self) -> None:
        with_browser_tool_is_url_valid("http://web-site.com/cgi-bin/perl.cgi?key1=value1&key2") is False
