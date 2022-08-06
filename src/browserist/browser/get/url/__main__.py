from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .current import get_current_url
from .from_image import get_url_from_image
from .from_images import get_url_from_images
from .from_link import get_url_from_link
from .from_links import get_url_from_links


class GetUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def current(self) -> str:  # type: ignore
        """Get URL of the current page."""

        if self._timeout_should_continue():
            return get_current_url(self._browser_driver)

    def from_image(self, xpath: str, timeout: float | None = None) -> str:  # type: ignore
        """Get URL source from image, e.g. <img> tag.

        This method assumes that the image shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_image(self._browser_driver, xpath, timeout)

    def from_images(self, xpath: str, timeout: float | None = None) -> list[str]:  # type: ignore
        """Get array of URLs from images, e.g. <img> tags. Assumes that the XPath targets multiple images."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_images(self._browser_driver, xpath, timeout)

    def from_link(self, xpath: str, timeout: float | None = None) -> str:  # type: ignore
        """Get URL from link, e.g. <a> tag or button.

        This method assumes that the link shouldn't be empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time)."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_link(self._browser_driver, xpath, timeout)

    def from_links(self, xpath: str, timeout: float | None = None) -> list[str]:  # type: ignore
        """Get array of URLs from links, e.g. <a> tags or buttons. Assumes that the XPath targets multiple links."""

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_links(self._browser_driver, xpath, timeout)
