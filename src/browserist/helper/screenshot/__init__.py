__all__ = ["controller", "default_file_name"]

from datetime import datetime

from . import controller


def default_file_name() -> str:
    """Example: \"Browserist screenshot 2022-02-12 at 22.12.34.png\""""

    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H.%M.%S")
    return f"Browserist screenshot {date} at {time}.png"


def save(driver: object, destination_dir: str, file_name: str) -> None:
    driver.save_screenshot(f"{destination_dir}{file_name}")  # type: ignore
