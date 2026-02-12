from browserist import Browser, factory
from browserist.constant import idle_timeout
from browserist.model.download.handler import DownloadHandler


def get(
    browser: Browser, download_dir_entries_before_download: list[str], uses_temporary_file: bool
) -> DownloadHandler:
    def ensure_uses_temporary_file_is_set_predictably(
        download_handler: DownloadHandler, value: bool
    ) -> DownloadHandler:
        """As not all browsers support temporary files, let's ensure that the `_uses_temporary_file` value is set as predicted by the test."""

        property(
            fget=lambda value: value,
            fset=setattr(download_handler, "_uses_temporary_file.setter", lambda: value),
            fdel=None,
        )
        return download_handler

    download_handler = factory.get.download_handler(
        browser_driver=browser._browser_driver,
        download_dir_entries_before_download=download_dir_entries_before_download,
        idle_download_timeout=idle_timeout.VERY_SHORT,
    )
    return ensure_uses_temporary_file_is_set_predictably(download_handler, uses_temporary_file)
