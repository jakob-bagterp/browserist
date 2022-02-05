from .get_methods import GetDriverMethods
from ..model.browser.base.driver import BrowserDriver
from ..model.driver_methods import DriverMethods

class OpenDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def url(self, url: str) -> None:
        """Open page."""

        self._driver.get(url)

    def url_if_not_current(self, url: str, ignore_trailing_slash: bool = True):
        """Open a URL if it isn't already the current URL. Useful when doing multiple operations on a page where."""

        # TODO: Evaluate without trailing slash
        # TODO: Ignore HTTP?(S) part of URL
        # TODO: Option to ignore parameters in URL
        current_url = GetDriverMethods(self._browser_driver).current_url()     
        if current_url != url:
            self.url(url)

    def url_in_new_tab(self, url: str):
        """Open a link in a new browser tab with support across browsers."""

        self._driver.execute_script(f"window.open('{url}', '_blank');")
        
        # TODO: Should the new tab be in focus? Could be an argument, e.g. ... focus_new_tab = False).
