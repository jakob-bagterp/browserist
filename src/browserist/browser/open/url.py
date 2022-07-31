from ...model.browser.base.driver import BrowserDriver
from ...model.type.url import URL


def open_url(browser_driver: BrowserDriver, url: str) -> None:
    url = URL(url)
    browser_driver.webdriver.get(url)  # type: ignore
