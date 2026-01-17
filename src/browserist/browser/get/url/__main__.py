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
            URL of the current page, e.g. `https://example.com`.

        Example:
            This will output the URL `https://example.com` in the terminal:

            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                current_url = browser.get.url.current()
                print(current_url)
            ```
        """

        if self._timeout_should_continue():
            return get_current_url(self._browser_driver)

    def current_domain(self) -> str:  # type: ignore
        """Get domain of the current page, e.g. `example.com`.

        Returns:
            Domain of the current page, e.g. `example.com`.

        Example:
            This will output the domain `example.com` in the terminal:

            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                current_domain = browser.get.url.current_domain()
                print(current_domain)
            ```
        """

        if self._timeout_should_continue():
            return get_current_domain(self._browser_driver)

    def from_image(self, xpath: str, timeout: float | None = None) -> str | None:  # type: ignore
        """Get the source URL of an `<img>` image element on the current page.

        Note:
            This method targets the `src` attribute of an `<img>` image element. And it assumes that the image isn't empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time).

        Args:
            xpath (str): XPath of the image. Should target an `<img>` tag.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            URL source of the image. If the image does not exist, `None` is returned.

        Example:
            ```python title="" linenums="1"
            image_url = browser.get.url.from_image("//xpath/to/img")
            print(image_url)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_image(self._browser_driver, xpath, timeout)

    def from_images(self, xpath: str, timeout: float | None = None) -> list[str | None]:  # type: ignore
        """Get list of source URLs of a group of `<img>` image elements on the current page.

        Note:
            This method targets the `src` attribute of the `<img>` image elements. And it assumes that the XPath targets multiple images.

        Args:
            xpath (str): XPath of the images. Should target `<img>` tags.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            List of image URLs. If an image does not exist, `None` is added to the list.

        Example:
            ```python title="" linenums="1"
            image_urls = browser.get.url.from_images("//img")
            for image_url in image_urls:
                print(image_url)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_images(self._browser_driver, xpath, timeout)

    def from_link(self, xpath: str, timeout: float | None = None) -> str | None:  # type: ignore
        """Get the source URL of an `<a>` link element on the current page.

        Note:
            This method targets the `href` attribute of the `<a>` link element. And it assumes that the link isn't empty and therefore will retry to get the URL (for better support of single-page apps with extended loading time).

        Args:
            xpath (str): XPath of the link. Should target an `<a>` tag.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            URL of the link. If the link does not exist, `None` is returned.

        Example:
            ```python title="" linenums="1"
            link_url = browser.get.url.from_link("//xpath/to/a")
            print(link_url)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_link(self._browser_driver, xpath, timeout)

    def from_links(self, xpath: str, timeout: float | None = None) -> list[str | None]:  # type: ignore
        """Get list of source URLs of a group of `<a>` link elements on the current page.

        Note:
            This method targets the `href` attribute of the `<a>` link elements. And it assumes that the XPath targets multiple links.

        Args:
            xpath (str): XPath of the links. Should target `<a>` tags.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            List of link URLs. If a link does not exist, `None` is added to the list.

        Example:
            ```python title="" linenums="1"
            link_urls = browser.get.url.from_links("//a")
            for link_url in link_urls:
                print(link_url)
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return get_url_from_links(self._browser_driver, xpath, timeout)
