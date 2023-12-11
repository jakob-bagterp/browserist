from pathlib import Path

from .....model.browser.base.driver import BrowserDriver
from .....model.driver_methods import DriverMethods
from .does_not_exist import wait_until_file_download_does_not_exist
from .exists import wait_until_file_download_exists


class WaitUntilDownloadFileDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def does_not_exist(self, file_name: str | Path, timeout: float | None = None) -> None:
        """Wait until a file download does not exist.

        Args:
            file_name (str | Path): Name of the file to watch in the download directory. The download directory is implicit and defined in the `download_dir` parameter of `BrowserSettings`.
            timeout (float | None, optional): In seconds. Timeout to wait for file to not exist. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_file_download_does_not_exist(self._browser_driver, file_name, timeout)

    def exists(self, file_name: str | Path, timeout: float | None = None) -> None:
        """Wait until a file download exists.

        Args:
            file_name (str | Path): Name of the file to watch in the download directory. The download directory is implicit and defined in the `download_dir` parameter of `BrowserSettings`.
            timeout (float | None, optional): In seconds. Timeout to wait for file to exist. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_file_download_exists(self._browser_driver, file_name, timeout)
