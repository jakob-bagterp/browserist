from ... import helper
from ..get.url.current import get_current_url
from .url import open_url


def open_url_if_not_current(driver: object, url: str, ignore_trailing_slash: bool = True) -> None:
    # TODO: Ignore HTTP?(S) part of URL
    # TODO: Option to ignore parameters in URL
    current_url = get_current_url(driver)
    if ignore_trailing_slash:
        current_url = helper.url.ensure_trailing_slash(current_url)
        url = helper.url.ensure_trailing_slash(url)
    if current_url != url:
        open_url(driver, url)
