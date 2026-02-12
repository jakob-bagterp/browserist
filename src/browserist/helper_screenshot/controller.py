from pathlib import Path

from .. import constant, helper, helper_screenshot
from ..model.browser.base.driver import BrowserDriver
from ..model.browser.base.settings import BrowserSettings
from ..model.screenshot import ScreenshotType
from ..model.type.file_png import FilePNG
from ..model.type.path import FilePath


def mediate_file_name(
    browser_driver: BrowserDriver, file_name: FilePNG | None, screenshot_type: ScreenshotType | None = None
) -> FilePNG:
    return helper_screenshot.file.get_default_name(browser_driver, screenshot_type) if file_name is None else file_name


def mediate_destination_dir(settings: BrowserSettings, destination_dir: str | Path | None = None) -> FilePath:
    if destination_dir is None:
        # As the default screenshot directory is the project's working directory, we don't need to create it.
        return settings._screenshot_dir
    destination_dir = FilePath(destination_dir)
    helper.directory.create_if_not_exists(destination_dir)
    return destination_dir


def mediate_temp_dir(destination_dir: FilePath) -> FilePath:
    """As the temporary directory will be a sub directory to the destination, this assumes that the destination directory has been defined by the controller."""

    temp_dir_path = destination_dir.path.joinpath(constant.screenshot.TEMP_DIR)
    temp_dir = FilePath(temp_dir_path)
    helper.directory.create_if_not_exists(temp_dir)
    return temp_dir
