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

    headless: If enabled, note that some interactable methods, e.g. "select", aren't supported.

    screenshot_dir: Destination directory for screenshot files. If not set, default directory is from where the script is executed.

    viewport: Emulate a viewport size upon initiation by either a common device or a custom value in pixels "(width, height)". If no value, the browser's default is used."""

    # TODO: Fix Pytest issue: "ValueError: 'type' in __slots__ conflicts with class variable"
    # __slots__ = ["type", "headless", "disable_images", "page_load_strategy", "path_to_executable", "screenshot_dir", "timeout", "viewport",
    #             "_path_to_executable", "_screenshot_dir"]

    type: BrowserType = BrowserType.EDGE if operating_system.is_windows() else BrowserType.CHROME
    headless: bool = False
    disable_images: bool = False
    page_load_strategy: PageLoadStrategy = PageLoadStrategy.NORMAL
    path_to_executable: str | Path | None = None
    screenshot_dir: str | Path = directory.PROJECT_WORKING_DIR
    timeout: TimeoutSettings = TimeoutSettings()
    viewport: DeviceViewportSize | tuple[int, int] | None = None

    def __post_init__(self) -> None:
        self._path_to_executable: FilePath | None = None if self.path_to_executable is None else FilePath(
            self.path_to_executable)
        self._screenshot_dir: FilePath = FilePath(self.screenshot_dir)
