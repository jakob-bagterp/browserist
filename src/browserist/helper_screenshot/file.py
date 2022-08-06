from .. import constant, helper
from ..helper.date_time import get_current_date_and_time, get_timestamp
from ..model.screenshot import ScreenshotType


def get_default_name(screenshot_type: ScreenshotType | None = None) -> str:
    """Example: \"Browserist screenshot 2022-02-12 at 22.12.34.png\""""

    date, time = get_current_date_and_time()
    appendix = "" if screenshot_type is None else f" ({screenshot_type.value})"
    return f"Browserist screenshot {date} at {time}{appendix}.png"


def get_temp_prefix_without_iterator_and_file_type() -> str:
    """Intended use: \"2022-02-12_22.12.34_temp_1.png\". Only returns the \"2022-02-12_22.12.34_temp\" part so remember to add the \"_1.png\" part."""

    timestamp = get_timestamp()
    return f"{timestamp}_{constant.screenshot.TEMP_FILE}"


def get_path(destination_dir: str, file_name: str) -> str:
    """Merge destination directory and file name into a single path. Assumes that the directory is valid and exists."""

    destination_dir = helper.directory.ensure_trailing_slash(destination_dir)
    return f"{destination_dir}{file_name}"
