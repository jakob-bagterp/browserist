from .url import open_url
from ..get.url.current import get_current_url

def open_url_if_not_current(driver: object, url: str, ignore_trailing_slash: bool = True) -> None:
    # TODO: Evaluate without trailing slash
    # TODO: Ignore HTTP?(S) part of URL
    # TODO: Option to ignore parameters in URL
    current_url = get_current_url(driver)
    if current_url != url:
        open_url(driver, url)
