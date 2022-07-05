__all__ = ["complete_page", "controller", "get_default_file_name"]


from ... import constant
from ...model.screenshot import ScreenshotType
from ..date_time import get_current_date, get_current_time
from . import complete_page, controller


def get_default_file_name(screenshot_type: ScreenshotType | None = None) -> str:
    """Example: \"Browserist screenshot 2022-02-12 at 22.12.34.png\""""

    date = get_current_date()
    time = get_current_time()
    appendix = "" if screenshot_type is None else f" ({screenshot_type.value})"
    return f"Browserist screenshot {date} at {time}{appendix}.png"


def get_temp_file_prefix_without_iterator_and_file_type() -> str:
    """Intended use: \"2022-02-12_22.12.34_temp_1.png\". Only returns the \"2022-02-12_22.12.34_temp\" part so remember to add the \"_1.png\" part."""

    date = get_current_date()
    time = get_current_time()
    return f"{date}_{time}_{constant.screenshot.TEMP_FILE}.png"


def generate_file_path(destination_dir: str, file_name: str) -> str:
    """Merge destination directory and file name into a single path. Assumes that the directory is valid and exists."""

    return f"{destination_dir}{file_name}"


def save(driver: object, destination_dir: str, file_name: str) -> None:
    file_path = generate_file_path(destination_dir, file_name)
    driver.save_screenshot(file_path)  # type: ignore


def save_element(element: object, destination_dir: str, file_name: str) -> None:
    """Reference: https://www.selenium.dev/documentation/webdriver/browser/windows/#takeelementscreenshot"""

    file_path = generate_file_path(destination_dir, file_name)
    element.screenshot(file_path)  # type: ignore
