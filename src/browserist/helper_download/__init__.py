__all__ = ["get_absolute_file_path"]

import os
from pathlib import Path

from ..model.browser.base.driver import BrowserDriver
from ..model.type.path import FilePath


def get_absolute_file_path(browser_driver: BrowserDriver, file_name: str | Path) -> FilePath:
    file_path = os.path.join(browser_driver.settings._download_dir, file_name)
    return FilePath(file_path)
