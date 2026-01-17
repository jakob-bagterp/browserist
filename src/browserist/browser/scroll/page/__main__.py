from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .down import scroll_page_down
from .to_end import scroll_to_end_of_page
from .to_top import scroll_to_top_of_page
from .up import scroll_page_up


class ScrollPageDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def down(self, pages: int = 1, delay_seconds: float = 1) -> None:
        """If possible, scroll number of pages down.

        Args:
            pages (int, optional): Number of pages to scroll down. Must be an integer of 1 or greater.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            Scroll single page down:

            ```python title=""
            browser.scroll.page.down()
            ```

            Scroll multiple pages down:

            ```python title=""
            browser.scroll.page.down(3)
            ```
        """

        if self._timeout_should_continue():
            scroll_page_down(self._browser_driver, pages, delay_seconds)

    def to_end(self, delay_seconds: float = 1) -> None:
        """If possible, scroll to end of the current page.

        Args:
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.page.to_end()
            ```
        """

        if self._timeout_should_continue():
            scroll_to_end_of_page(self._browser_driver, delay_seconds)

    def to_top(self, delay_seconds: float = 1) -> None:
        """If possible, scroll to top of the current page.

        Args:
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            ```python title=""
            browser.scroll.page.to_top()
            ```
        """

        if self._timeout_should_continue():
            scroll_to_top_of_page(self._browser_driver, delay_seconds)

    def up(self, pages: int = 1, delay_seconds: float = 1) -> None:
        """If possible, scroll number of pages up.

        Args:
            pages (int, optional): Number of pages to scroll up. Must be an integer of 1 or greater.
            delay_seconds (float, optional): Option to add custom delay in seconds to ensure the view is updated after scroll.

        Example:
            Scroll single page up:

            ```python title=""
            browser.scroll.page.up()
            ```

            Scroll multiple pages up:

            ```python title=""
            browser.scroll.page.up(3)
            ```
        """

        if self._timeout_should_continue():
            scroll_page_up(self._browser_driver, pages, delay_seconds)
