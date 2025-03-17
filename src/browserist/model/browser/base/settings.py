from dataclasses import dataclass
from pathlib import Path

from ....constant import directory
from ....helper import operating_system
from ....model.browser.base.proxy import ProxySettings
from ....model.viewport.device import DeviceViewportSize
from ...type.path import FilePath
from .page_load_strategy import PageLoadStrategy
from .timeout import TimeoutSettings
from .type import BrowserType


@dataclass(kw_only=True)
class BrowserSettings:
    """Class to configure the browser driver.

    Args:
        type (BrowserType, optional): Set [browser type](../../settings/browser-types.md), e.g. Chrome, Edge, Firefox, etc.
        headless (bool, optional): Run the browser in [headless mode](../../performance/headless.md). May not be supported by all browsers, or some interaction methods, e.g. select, may not be supported.
        disable_images (bool, optional): [Neither request nor render images](../../performance/disable-images.md), which typically improves loading speed. May not be supported by all browsers.
        page_load_strategy (PageLoadStrategy, optional): Set [page load strategy](../../settings/page-load-strategy.md).
        path_to_executable (str | Path | None, optional): If the browser executable isn't in a default folder, select which file to use.
        download_dir (str | Path, optional): Set where to save [downloads](../../user-guide/download-files.md). Default is the `Downloads` folder of the user.
        screenshot_dir (str | Path, optional): Set where to save [sreenshots](../../user-guide/screenshots.md). Default is the `Downloads` folder of the user.
        timeout (TimeoutSettings, optional): Set [timeout strategy and time](../../settings/timeout-strategy.md).
        viewport (DeviceViewportSize | tuple[int, int] | None, optional): Emulate [viewport size](../../settings/viewport.md) as device or set custom value in pixels. If not set, the browser's default size is used.
        check_connection (bool, optional): Check whether there is an [internet connection](../../settings/check-connection.md) before starting the browser. Bypass the check by setting it to `False`.
        user_agent (str | None, optional): Set a custom [user agent](../../settings/user-agent.md) to override the default user agent. If not set, the browser's default user agent is used.
        proxy (str | ProxySettings | None, optional): Enable a custom [proxy server](../../settings/proxy.md) for the browser. If not using `ProxySettings`, use a string containing IP address and port number. For example, `http://127.0.0.1:8080` for a public proxy or `http://username:password@127.0.0.1:8080` for a private proxy that requires authentication.

    Example:
        Use Firefox as browser type:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(browser_type=BrowserType.FIREFOX)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use browser in headless mode and with images disabled:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(headless=True, disable_images=True)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use custom directory for screenshots:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(screenshot_dir="/screenshots/folder")

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
            browser.screenshot.visible_portion()
        ```

        Use custom viewport size:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(viewport=(1024, 768))

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use custom `User-agent` in the request header:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(user_agent="MyUserAgent")

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
            user_agent = browser.user_agent.get()
            print(user_agent)
        ```

        How the print output appears in the terminal:

        ```shell title=""
        MyUserAgent
        ```

        How to disable checking for an internet connection:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(check_connection=False)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use a custom proxy with a basic URL:

        ```python title="" linenums="1" hl_lines="3"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(proxy="http://127.0.0.1:8080")

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use a custom proxy with a `ProxySettings` configuration class:

        ```python title="" linenums="1" hl_lines="3-6"
        from browserist import Browser, BrowserSettings, ProxySettings, ProxyProtocol

        proxy_settings = ProxySettings(
            ip="127.0.0.1",
            port=8080,
            protocol=ProxyProtocol.HTTP)

        settings = BrowserSettings(proxy=proxy_settings)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    # TODO: Fix Pytest issue: "ValueError: 'type' in __slots__ conflicts with class variable"
    # __slots__ = ["type", "headless", "disable_images", "page_load_strategy", "path_to_executable", "screenshot_dir", "timeout", "viewport",
    #             "check_connection", "user_agent", "proxy", "_proxy_url", "_path_to_executable", "_screenshot_dir"]

    type: BrowserType = BrowserType.EDGE if operating_system.is_windows() else BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False
    page_load_strategy: PageLoadStrategy = PageLoadStrategy.NORMAL
    path_to_executable: str | Path | None = None
    download_dir: str | Path = directory.DOWNLOADS_DIR
    screenshot_dir: str | Path = directory.DOWNLOADS_DIR
    timeout: TimeoutSettings = TimeoutSettings()
    viewport: DeviceViewportSize | tuple[int, int] | None = None
    check_connection: bool = True
    user_agent: str | None = None
    proxy: str | ProxySettings | None = None

    def __post_init__(self) -> None:
        self._path_to_executable: FilePath | None = None if self.path_to_executable is None else FilePath(
            self.path_to_executable)
        self._download_dir: FilePath = FilePath(self.download_dir)
        self._screenshot_dir: FilePath = FilePath(self.screenshot_dir)
        self._proxy_url: str | None = self.proxy.get_url() if isinstance(self.proxy, ProxySettings) else self.proxy
