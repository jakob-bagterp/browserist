from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .page_source import get_page_source


class GetHtmlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def page_source(self) -> str:  # type: ignore
        """Get page source of the current page.

        Returns:
            Page source.

        Example:
            ```python title="" linenums="1"
            page_source = browser.get.html.page_source()
            print(page_source)
            ```
        """

        if self._timeout_should_continue():
            return get_page_source(self._browser_driver)
