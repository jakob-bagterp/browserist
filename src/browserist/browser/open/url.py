from ...model.browser.base.driver import BrowserDriver
from ...model.type.url import URL


def open_url(browser_driver: BrowserDriver, url: str) -> None:
    url = URL(url)
    driver = browser_driver.get_webdriver()
    driver.get(url)
