from dataclasses import dataclass
from pathlib import Path

from ....constant import directory
from ....helper import operating_system
from ....model.viewport.device import DeviceViewportSize
from ...type.path import FilePath
from .page_load_strategy import PageLoadStrategy
from .timeout.settings import TimeoutSettings
from .type import BrowserType


@dataclass(kw_only=True)
class BrowserSettings:
    """Class to configure the browser driver.

    Args:
        type (BrowserType, optional): Set [browser type](../../user-guide/settings/browser-types.md), e.g. Chrome, Edge, Firefox, etc.
        headless (bool, optional): Run the browser in [headless mode](../../user-guide/performance/headless.md). May not be supported by all browsers, or some interaction methods, e.g. select, may not be supported.
        disable_images (bool, optional): [Neither request nor render images](../../user-guide/performance/disable-images.md), which typically improves loading speed. May not be supported by all browsers.
        page_load_strategy (PageLoadStrategy, optional): Set [page load strategy](../../user-guide/settings/page-load-strategy.md).
        path_to_executable (str | Path | None, optional): If the browser executable isn't in a default folder, select which file to use.
        download_dir (str | Path, optional): Set where to save downloads. Default is the `Downloads` folder of the user.
        screenshot_dir (str | Path, optional): Set where to save sreenshots. Default is the `Downloads` folder of the user.
        timeout (TimeoutSettings, optional): Set [timeout strategy and time](../../user-guide/settings/timeout-strategy.md).
        viewport (DeviceViewportSize | tuple[int, int] | None, optional): Emulate [viewport size](../../user-guide/settings/viewport.md) as device or set custom value in pixels. If not set, the browser's default size is used.
        check_connection (bool, optional): Check that there is an internet connection before starting the browser. Bypass the check by setting it to `False`.

    Example:
        Use Firefox as browser type:

        ```python title="" linenums="1"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(browser_type=BrowserType.FIREFOX)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use browser in headless mode and with images disabled:

        ```python title="" linenums="1"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(headless=True, disable_images=True)

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```

        Use custom directory for screenshots:

        ```python title="" linenums="1"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(screenshot_dir="/screenshots/folder")

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
            browser.screenshot.visible_portion()
        ```

        Use custom viewport size:

        ```python title="" linenums="1"
        from browserist import Browser, BrowserSettings

        settings = BrowserSettings(viewport=(1024, 768))

        with Browser(settings) as browser:
            browser.open.url("https://example.com")
        ```
    """

    # TODO: Fix Pytest issue: "ValueError: 'type' in __slots__ conflicts with class variable"
    # __slots__ = ["type", "headless", "disable_images", "page_load_strategy", "path_to_executable", "screenshot_dir", "timeout", "viewport",
    #             "check_connection", "_path_to_executable", "_screenshot_dir"]

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

    def __post_init__(self) -> None:
        self._path_to_executable: FilePath | None = None if self.path_to_executable is None else FilePath(
            self.path_to_executable)
        self._download_dir: FilePath = FilePath(self.download_dir)
        self._screenshot_dir: FilePath = FilePath(self.screenshot_dir)
