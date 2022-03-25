from ....constant import timeout
from ....model.browser.base.driver import BrowserDriver
from ....model.browser.base.settings import BrowserSettings
from ....model.driver_methods import DriverMethods
from .current import get_current_url
from .from_image import get_url_from_image
from .from_link import get_url_from_link
from .from_multiple_images import get_url_from_multiple_images
from .from_multiple_links import get_url_from_multiple_links


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

    def from_link(self, xpath: str, timeout: int = timeout.DEFAULT) -> str:
        """Get URL from link, e.g. <a> tag or button.

        This method assumes that the link shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        return get_url_from_link(self._driver, xpath, timeout)

    def from_multiple_images(self, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
        """Get array of URLs from images, e.g. <img> tags. Assumes that the XPath targets multiple images."""

        return get_url_from_multiple_images(self._driver, xpath, timeout)

    def from_multiple_links(self, xpath: str, timeout: int = timeout.DEFAULT) -> list[str]:
        """Get array of URLs from links, e.g. <a> tags or buttons. Assumes that the XPath targets multiple links."""

        return get_url_from_multiple_links(self._driver, xpath, timeout)
