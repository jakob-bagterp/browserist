from .....model.browser.base.driver import BrowserDriver
from .....model.driver_methods import DriverMethods
from .does_not_exist import wait_until_download_file_does_not_exist
from .exists import wait_until_download_file_exists
from .size_does_not_increase import wait_until_download_file_size_does_not_increase


class WaitUntilDownloadFileDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def does_not_exist(self, file_name: str, timeout: float | None = None) -> None:
        """Wait until a file download does not exist, e.g. a temporary file created by the browser until download is complete.

        Args:
            file_name (str): Name of the file to watch in the download directory, e.g. `file.zip`. The download directory is implicitly defined in the `download_dir` parameter of `BrowserSettings`.
            timeout (float | None, optional): In seconds. Timeout to wait for file to not exist. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.click.download("//xpath/to/button", expected_file_name="file.zip"))
                browser.wait.until.download_file.does_not_exist("file.zip.download")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_download_file_does_not_exist(self._browser_driver, file_name, timeout)

    def exists(self, file_name: str, timeout: float | None = None) -> None:
        """Wait until a file download exists.

        Args:
            file_name (str): Name of the file to watch in the download directory, e.g. `file.zip`. The download directory is implicitly defined in the `download_dir` parameter of `BrowserSettings`.
            timeout (float | None, optional): In seconds. Timeout to wait for file to exist. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.click.download("//xpath/to/button", expected_file_name="file.zip"))
                browser.wait.until.download_file.exists("file.zip")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            wait_until_download_file_exists(self._browser_driver, file_name, timeout)

    def size_does_not_increase(self, file_name: str, idle_download_timeout: float | None = None) -> None:
        """Wait until a file under download no longer exists or increases in size, for example a temporary file created by the browser until a download is complete.

        Args:
            file_name (str): Name of the file to watch in the download directory, e.g. `file.zip`. The download directory is implicitly defined in the `download_dir` parameter of `BrowserSettings`.
            idle_download_timeout (float | None, optional): In seconds. Timeout to wait for file size to not increase, which is constantly renewed as long as the file size increases. If `None`, the global idle download timeout setting is used (default 3 seconds).

        Example:
            ```python title="" linenums="1" hl_lines="6"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.click.download("//xpath/to/button", expected_file_name="file.zip"))
                browser.wait.until.download_file.size_does_not_increase("file.zip")
            ```
        """

        if self._timeout_should_continue():
            idle_download_timeout = self._mediate_idle_download_timeout(idle_download_timeout)
            wait_until_download_file_size_does_not_increase(self._browser_driver, file_name, idle_download_timeout)
