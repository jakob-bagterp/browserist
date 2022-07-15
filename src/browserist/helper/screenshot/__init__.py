__all__ = ["controller", "default_file_name"]

from datetime import datetime

from ...model.screenshot import ScreenshotType
from . import controller


def default_file_name(screenshot_type: ScreenshotType | None = None) -> str:
    """Example: \"Browserist screenshot 2022-02-12 at 22.12.34.png\""""

    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H.%M.%S")
    appendix = "" if screenshot_type is None else f" ({screenshot_type.value})"
    return f"Browserist screenshot {date} at {time}{appendix}.png"


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
