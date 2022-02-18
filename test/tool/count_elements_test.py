from browserist import Browser
from _config.browser_settings import default
from _helper import internal_url

class TestToolCountElements():
    def test_tool_count_elements(self) -> None:
        with Browser(default.HEADLESS) as browser:
            browser.open.url(internal_url.EXAMPLE_COM)
            assert browser.tool.count_elements("/html/body/div/p") == 2
