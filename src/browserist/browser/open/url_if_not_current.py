from ... import helper
from ...model.browser.base.driver import BrowserDriver
from ...model.type.url import URL
from ..get.url.current import get_current_url
from .url import open_url


def open_url_if_not_current(browser_driver: BrowserDriver,
                            url: str,
                            ignore_trailing_slash: bool = True,
                            ignore_parameters: bool = False,
                            ignore_https: bool = False) -> None:

    url = URL(url)
    current_url = get_current_url(browser_driver)
    url_pattern = helper.url.compile_comparison_to_regex_pattern(url, ignore_trailing_slash, ignore_parameters, ignore_https)
    if not url_pattern.fullmatch(current_url):
        open_url(browser_driver, url)
