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
    if ignore_https:
        current_url, url = helper.url.mediate_https(current_url, url)
    if ignore_parameters:
        current_url = helper.url.remove_parameters(current_url)
        url = helper.url.remove_parameters(url)
    if ignore_trailing_slash:
        current_url = helper.url.ensure_trailing_slash(current_url)
        url = helper.url.ensure_trailing_slash(url)
    if current_url != url:
        open_url(browser_driver, url)
