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
        """Click button on the current page.

        Args:
            xpath (str): XPath of the button element.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            ```python title=""
            browser.click.button("//xpath/to/button")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_button(self._browser_driver, xpath, timeout)

    def button_if_contains_text(self, xpath: str, regex: str, ignore_case: bool = True, timeout: float | None = None) -> None:
        """Click button on the current page if it contains certain text.

        Args:
            xpath (str): XPath of the button element.
            regex (str): Regular expression or text to search for. The condition works for both ordinary text (e.g. `Submit`) or regular expression (e.g. `r"colou?r"`). Note it's a search for text, not a strict text match.
            ignore_case (bool, optional): Ignore case when searching for text.
            timeout (float | None, optional): In seconds. Timeout to wait for element. If `None`, the global timeout setting is used (default 5 seconds).

        Example:
            Without regular expression:

            ```python title=""
            browser.click.button_if_contains_text("//xpath/to/button", "Save")
            ```

            With regular expression:

            ```python title=""
            browser.click.button_if_contains_text("//xpath/to/button", r"^Submit")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            click_button_if_contains_text(self._browser_driver, xpath, regex, ignore_case, timeout)

    def download(self, xpath: str, timeout: float | None = None, await_download: bool = False, expected_file_name: str | None = None, idle_download_timeout: float | None = None) -> None:
        """Click button on the current page and download file.

        Args:
            xpath (str): XPath of the download button element.
            timeout (float | None, optional): In seconds. Timeout to wait for button element. If `None`, the global timeout setting is used (default 5 seconds).
            await_download (bool, optional): Set to `False` to download the file in the background – this will also bypass the `expected_file_name` and `idle_download_timeout` parameters. Set to `True` to wait for the download to complete.
            expected_file_name (str | None, optional): Expected file name to determine when the download is complete. If `None`, this may be slower as Browserist will attempt to guess the file name by monitoring changes in the download directory.
            idle_download_timeout (float | None, optional): In seconds. Timeout to wait for file size to not increase, which is constantly renewed as long as the file size increases. If `None`, the global idle download timeout setting is used (default 3 seconds).

        Info: Download Directory
            The download directory is implicitly defined in the [`download_dir` parameter of `BrowserSettings`](../../settings/overview.md).

            Avoid that multiple browser instances have access to the same download directory. As Browserist monitors the download directory for file changes, it may cause unexpected behaviour if multiple files are downloaded to the same directory at the same time.

        Example:
            Examples in context:

            ```python title="" linenums="1" hl_lines="5-7"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                browser.click.download("//xpath/to/button")
                browser.click.download("//xpath/to/button", await_download=True)
                browser.click.download("//xpath/to/button", await_download=True, expected_file_name="file.zip")
            ```

            Download file in background without waiting. If the browser closes during a download, the download may be aborted or left incomplete:

            ```python title="" linenums="5"
                browser.click.download("//xpath/to/button")
            ```

            Download file and wait for download to complete. This will attempt to guess the file name, which may be slower:

            ```python title="" linenums="6"
                browser.click.download("//xpath/to/button", await_download=True)
            ```

            Download expected file name and wait for download to complete. It's faster if you know the file name:

            ```python title="" linenums="7"
                browser.click.download("//xpath/to/button", await_download=True, expected_file_name="file.zip")
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            idle_download_timeout = self._mediate_idle_download_timeout(idle_download_timeout)
            click_download_button(self._browser_driver, xpath, timeout, await_download, expected_file_name, idle_download_timeout)

    def download_and_get_file_path(self, xpath: str, timeout: float | None = None, idle_download_timeout: float | None = None) -> Path:  # type: ignore
        """Click button on the current page to download file and get file path once download is complete. As downloads are automatically handled by the browser, this is useful if you don't know the file name beforehand.

        Args:
            xpath (str): XPath of the download button element.
            timeout (float | None, optional): In seconds. Timeout to wait for button element. If `None`, the global timeout setting is used (default 5 seconds).
            idle_download_timeout (float | None, optional): In seconds. Timeout to wait for file size to not increase, which is constantly renewed as long as the file size increases. If `None`, the global idle download timeout setting is used (default 3 seconds).

        Returns:
            Path to the downloaded file. Return type is the standard library `pathlib.Path`.

        Info: Download Directory
            The download directory is implicitly defined in the [`download_dir` parameter of `BrowserSettings`](../../settings/overview.md).

            Avoid that multiple browser instances have access to the same download directory. As Browserist monitors the download directory for file changes, it may cause unexpected behaviour if multiple files are downloaded to the same directory at the same time.

        Example:
            ```python title="" linenums="1" hl_lines="5"
            from browserist import Browser

            with Browser() as browser:
                browser.open.url("https://example.com")
                file_path = browser.click.download_and_get_file_path("//xpath/to/button")
            ```

            The return type is `Path` from the standard [`pathlib`](https://docs.python.org/3/library/pathlib.html) library, and so you can easily get the file name or absolute path.

            For instance, this will output the file name `file.zip` in the terminal:

            ```python title="" linenums="6"
                print(file_path.name)
            ```

            And this will output the absolute file path `/home/user/downloads/file.zip` in the terminal:

            ```python title="" linenums="7"
                print(file_path.absolute())
            ```
        """

        if self._timeout_should_continue():
            timeout = self._mediate_timeout(timeout)
            idle_download_timeout = self._mediate_idle_download_timeout(idle_download_timeout)
            return click_download_button_and_get_file_path(self._browser_driver, xpath, timeout, idle_download_timeout)
