from .. import constant
from ..browser.get.url.current_domain import get_current_domain
from ..helper.date_time import get_current_date_and_time, get_timestamp
from ..model.browser.base.driver import BrowserDriver
from ..model.screenshot import ScreenshotType
from ..model.type.file_png import FilePNG
from ..model.type.path import FilePath


def get_default_name(browser_driver: BrowserDriver, screenshot_type: ScreenshotType | None = None) -> FilePNG:
    """Example: \"Browserist screenshot of example.com on 2022-02-12 at 22.12.34.png\""""

    domain = get_current_domain(browser_driver)
    date, time = get_current_date_and_time()
    appendix = "" if screenshot_type is None else f" ({screenshot_type.value})"
    return FilePNG(f"Browserist screenshot of {domain} on {date} at {time}{appendix}.png")


def get_temp_prefix_without_iterator_and_file_type() -> str:
    """Intended use: \"2022-02-12_22.12.34_temp_1.png\". Only returns the \"2022-02-12_22.12.34_temp\" part so remember to add the \"_1.png\" part."""

    timestamp = get_timestamp()
    return f"{timestamp}_{constant.screenshot.TEMP_FILE}"


def get_path(file_name: FilePNG, destination_dir: FilePath) -> FilePath:
    """Merge destination directory and file name into a single path. Assumes that the directory is valid and exists."""

    destination_dir_path = destination_dir.path.joinpath(file_name)
    return FilePath(destination_dir_path)
