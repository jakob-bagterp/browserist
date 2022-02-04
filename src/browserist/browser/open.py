from ..model.browser.base.driver import BrowserDriver

class Open():
    def __init__(self, browser_driver: BrowserDriver) -> None:
        self._driver: object = browser_driver.webdriver

    def url(self, url: str) -> None:
        """Open page."""

        self._driver.get(url)
