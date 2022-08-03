from dataclasses import dataclass
from enum import Enum, unique

from .. import helper, screenshot_helper
from .type.file_png import FilePNG


@unique
class ScreenshotType(Enum):
    """Class to define screenshot type, e.g. complete page, visible portion, element."""

    COMPLETE_PAGE = "complete page"
    ELEMENT = "element"
    VISIBLE_PORTION = "visible portion"


@dataclass(kw_only=True)
class ScreenshotTempDataHandler():
    """Class to handle iteration details and general data for screenshot of complete page, e.g. file and directory names."""

    __slots__ = ["destination_dir", "destination_file_path",
                 "_all_temp_file_paths", "_temp_file_prefix", "_iteration", "_temp_dir"]

    destination_dir: str
    destination_file_path: str

    def __post_init__(self) -> None:
        self.destination_file_path = FilePNG(self.destination_file_path)
        self._temp_dir: str = screenshot_helper.controller.mediate_temp_dir(self.destination_dir)
        self._all_temp_file_paths: list[str] = []
        self._temp_file_prefix: str = screenshot_helper.file.get_temp_prefix_without_iterator_and_file_type()
        self._iteration: int = 1

    def get_temp_file_name(self) -> str:
        return f"{self._temp_file_prefix}_{self._iteration}.png"

    def get_temp_file_path(self) -> str:
        temp_file_name = self.get_temp_file_name()
        return screenshot_helper.file.get_path(self._temp_dir, temp_file_name)

    def save_screenshot(self, driver: object) -> None:
        temp_file_path = self.get_temp_file_path()
        screenshot_helper.save(driver, temp_file_path)
        self._all_temp_file_paths.append(temp_file_path)

    def increment_iteration(self) -> None:
        self._iteration += 1

    async def merge_temp_files_into_final_screenshot(self) -> None:
        screenshot_helper.merge_images(self._all_temp_file_paths, self.destination_file_path)

    def remove_temp_files(self) -> None:
        helper.file.remove(self._all_temp_file_paths)
