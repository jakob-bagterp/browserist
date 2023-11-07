from ....model.browser.base.driver import BrowserDriver
from ....model.driver_methods import DriverMethods
from .current import get_current_url
from .current_domain import get_current_domain
from .from_image import get_url_from_image
from .from_images import get_url_from_images
from .from_link import get_url_from_link
from .from_links import get_url_from_links


class GetUrlDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def current(self) -> str:  # type: ignore
        """Get URL of the current page, e.g. `https://example.com`.

        Returns:
            str: URL of the current page, e.g. `https://example.com`.
        """

        if self._timeout_should_continue():
            return get_current_url(self._browser_driver)

    def current_domain(self) -> str:  # type: ignore
        """Get domain of the current page, e.g. `example.com`.

        Returns:
            str: Domain of the current page, e.g. `example.com`.
        """

        if self._timeout_should_continue():
            return get_current_domain(self._browser_driver)

    def from_image(self, xpath: str, timeout: float | None = None) -> str | None:  # type: ignore
        """Get URL source from image, i.e. `<img>` tag.

        Note:
            This method assumes that the image isn't empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time).

        Args:
            xpath (str): XPath of the image. Should target an `<img>` tag.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            str | None: URL source of the image. If the image does not exist, `None` is returned.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_image(self._browser_driver, xpath, timeout)

    def from_images(self, xpath: str, timeout: float | None = None) -> list[str | None]:  # type: ignore
        """Get list of URLs from images, i.e. `<img>` tags. Assumes that the XPath targets multiple images.

        Args:
            xpath (str): XPath of the images. Should target `<img>` tags.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            list[str | None]: List of image URLs. If an image does not exist, `None` is added to the list.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_images(self._browser_driver, xpath, timeout)

    def from_link(self, xpath: str, timeout: float | None = None) -> str | None:  # type: ignore
        """Get URL from link or button, i.e. `<a>` tag.

        Note:
            This method assumes that the link isn't empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time).

        Args:
            xpath (str): XPath of the link. Should target an `<a>` tag.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            str | None: URL of the link. If the link does not exist, `None` is returned.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_link(self._browser_driver, xpath, timeout)

    def from_links(self, xpath: str, timeout: float | None = None) -> list[str | None]:  # type: ignore
        """Get array of URLs from links or buttons, i.e. `<a>` tags. Assumes that the XPath targets multiple links.

        Args:
            xpath (str): XPath of the links. Should target `<a>` tags.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            list[str | None]: List of link URLs. If a link does not exist, `None` is added to the list.
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_links(self._browser_driver, xpath, timeout)
