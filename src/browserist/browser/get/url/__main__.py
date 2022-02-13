from .current import get_current_url
from .from_image import get_url_from_image
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from ....constant import timeout

class GetUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver, settings: BrowserSettings) -> None:
        super().__init__(browser_driver, settings)

    def current(self) -> str:
        """Get URL of the current page."""

        return get_current_url(self._driver)

    def from_image(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get URL source from image, e.g. <img> tag.

        This method assumes that the image shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        return get_url_from_image(self._driver, xpath, timeout)
