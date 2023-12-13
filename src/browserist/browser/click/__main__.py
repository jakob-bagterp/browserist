from pathlib import Path

from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .button import click_button
from .button_if_contains_text import click_button_if_contains_text
from .download import click_download_button
from .download_and_get_file_path import click_download_button_and_get_file_path


class ClickDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def button(self, xpath: str, timeout: float | None = None) -> None:
        """Click button.

        Args:
            xpath (str): XPath of the button element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_button(self._browser_driver, xpath, timeout)

    def button_if_contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: float | None = None) -> None:
        """Click button if it contains certain text.

        Args:
            xpath (str): XPath of the button element.
            regex (str): Regular expression or text to search for. The condition works for both ordinary text (e.g. `"Submit"`) or regular expression (e.g. `r"colou?r"`). Note it's a search for text, not a strict text match.
            ignore_case (bool, optional): Ignore case when searching for text.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_button_if_contains_text(self._browser_driver, xpath, regex, ignore_case, timeout)

    def download(self, xpath: str, timeout: float | None = None) -> None:
        """Click button and download file.

        Args:
            xpath (str): XPath of the download button element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_download_button(self._browser_driver, xpath, timeout)

    def download_and_get_file_path(self, xpath: str, timeout: float | None = None) -> Path:  # type: ignore
        """Click button to download file and get file path once download is complete.

        Args:
            xpath (str): XPath of the download button element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Returns:
            Path: Path to the downloaded file. Return type is the standard library `pathlib.Path`.

        Example:
            ```python title=""
            from pathlib import Path
            from browserist import Browser

            with Browser(settings) as browser:
                browser.open.url("https://example.com")
                file_path = browser.click.download_and_get_file_path("//button[@id='download']")
                print("File name:", file_path.name)
                # File name: file.zip
                print("Absolute file path:",file_path.absolute())
                # Absolute path: "/home/user/downloads/file.zip"
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            return click_download_button_and_get_file_path(self._browser_driver, xpath, timeout)
