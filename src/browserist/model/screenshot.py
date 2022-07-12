from dataclasses import dataclass
from enum import Enum, unique

from .. import helper


@unique
class ScreenshotType(Enum):
    """Class to define screenshot type, e.g. complete page, visible portion, element."""

    COMPLETE_PAGE = "complete page"
    ELEMENT = "element"
    VISIBLE_PORTION = "visible portion"


@dataclass(kw_only=True)
class ScreenshotTempDataHandler():
    """Class to handle iteration details and general data for screenshot of complete page, e.g. file and directory names."""

    __slots__ = ["destination_dir", "file_path", "_all_temp_file_paths", "_temp_file_prefix", "_iteration", "_temp_dir"]

    destination_dir: str
    file_path: str
    _all_temp_file_paths: list[str] = []
    _temp_file_prefix: str = helper.screenshot.file.get_temp_prefix_without_iterator_and_file_type()
    _iteration: int = 1

    def __post_init__(self) -> None:
        self._temp_dir: str = helper.screenshot.controller.mediate_temp_dir(self.destination_dir)

    def get_temp_file_name(self) -> str:
        return f"{self._temp_file_prefix}_{self._iteration}.png"

    def get_temp_file_path(self) -> str:
        return helper.screenshot.file.get_path(self._temp_dir, self.get_temp_file_name())

    def next_iteration(self) -> None:
        temp_file_path = self.get_temp_file_path()
        self._all_temp_file_paths.append(temp_file_path)
        self._iteration += 1

    def merge_temp_images_into_final_screenshot(self) -> None:
        helper.screenshot.merge_images(self._all_temp_file_paths, self.file_path)

    def remove_temp_files(self) -> None:
        helper.file.remove(self._all_temp_file_paths)
