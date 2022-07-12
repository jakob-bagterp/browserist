from dataclasses import dataclass
from enum import Enum, unique

from .. import helper


@unique
class ScreenshotType(Enum):
    """Class to define screenshot type, e.g. complete page, visible portion, element."""

    COMPLETE_PAGE = "complete page"
    ELEMENT = "element"
    VISIBLE_PORTION = "visible portion"


@dataclass(kw_only=True, slots=True)
class ScreenshotTempDataHandler():
    """Class to handle iteration details and general data for screenshot of complete page, e.g. file and directory names."""

    destination_dir: str
    file_path: str
    all_temp_file_paths: list[str] = []
    _temp_file_prefix: str = helper.screenshot.file.get_temp_prefix_without_iterator_and_file_type()
    _iteration: int = 1

    # TODO: Should be static attribute: temp_dir
    def get_temp_dir(self) -> str:
        return helper.screenshot.controller.mediate_temp_dir(self.destination_dir)

    def get_temp_file_name(self) -> str:
        return f"{self._temp_file_prefix}_{self._iteration}.png"

    def get_temp_file_path(self) -> str:
        return helper.screenshot.file.get_path(self.get_temp_dir(), self.get_temp_file_name())

    def next_iteration(self) -> None:
        temp_file_path = self.get_temp_file_path()
        self.all_temp_file_paths.append(temp_file_path)
        self._iteration += 1

    def merge_temp_images_into_final_screenshot(self) -> None:
        helper.screenshot.merge_images(self.all_temp_file_paths, self.file_path)

    def remove_temp_files(self) -> None:
        helper.file.remove(self.all_temp_file_paths)
