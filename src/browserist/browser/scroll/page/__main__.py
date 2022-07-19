from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .down import scroll_page_down
from .to_end import scroll_to_end_of_page
from .to_top import scroll_to_top_of_page
from .up import scroll_page_up


class ScrollPageDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def down(self, delay_seconds: float = 1) -> None:
        """If possible, scroll page down. Add custom delay in seconds to ensure the view is updated after scroll."""

        scroll_page_down(self._driver, delay_seconds)

    def to_end(self, delay_seconds: float = 1) -> None:
        """If possible, scroll to end of page. Add custom delay in seconds to ensure the view is updated after scroll."""

        scroll_to_end_of_page(self._driver, delay_seconds)

    def to_top(self, delay_seconds: float = 1) -> None:
        """If possible, scroll to top of page. Add custom delay in seconds to ensure the view is updated after scroll."""

        scroll_to_top_of_page(self._driver, delay_seconds)

    def up(self, delay_seconds: float = 1) -> None:
        """If possible, scroll page up. Add custom delay in seconds to ensure the view is updated after scroll."""

        scroll_page_up(self._driver, delay_seconds)
