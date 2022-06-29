from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .page_down import scroll_page_down


class ScrollPageDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def page_down(self) -> None:
        """If possible, scroll page down."""

        scroll_page_down(self._driver)
