from browserist import Browser, factory
from browserist.constant import idle_timeout
from browserist.model.download.handler import DownloadHandler


def get(browser: Browser, download_dir_entries_before_download: list[str]) -> DownloadHandler:
    def ensure_uses_temporary_file_is_true(download_handler: DownloadHandler) -> DownloadHandler:
        property(
            fget=lambda value: True,
            fset=setattr(download_handler, "_uses_temporary_file.setter", lambda: True),
            fdel=None
        )
        return download_handler

    download_handler = factory.get.download_handler(
        browser_driver=browser._browser_driver,
        download_dir_entries_before_download=download_dir_entries_before_download,
        idle_download_timeout=idle_timeout.VERY_SHORT,
    )
    return ensure_uses_temporary_file_is_true(download_handler)
