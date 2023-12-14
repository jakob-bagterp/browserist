import os
from abc import ABC, abstractmethod

from ..... import helper
from ....type.path import FilePath


class DownloadHandler(ABC):
    """Abstract class that contains the download handler methods for various browser types."""

    def __init__(self) -> None:
        self.temporary_file: FilePath | None = None
        self.file: FilePath | None = None

    @property
    @abstractmethod
    def uses_temporary_file(self) -> bool:
        """Configuration property to set if the browser uses temporary files for downloads."""

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def temporary_file_predicts_final_file(self) -> bool:
        """Some browsers add a temporary file extension to the download file, making it easier to determine what the name of the final file is."""

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def temporary_file_extension(self) -> str:
        """Property to define the temporary file extension used by the given browser.

        For example: `.download` for Safari, `.crdownload` for Chrome, `.part` for Firefox, etc."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def is_temporary_file(self, download_dir: FilePath, file_name: str) -> bool:
        """If browsers use temporary download files, they all have different formats. Check whether a file name appears to be a temporary file for the specific browser."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def get_temporary_file_without_extension(self) -> FilePath | None:
        """If a browser's temporary download file predicts the final file name – for instance by adding an extension – this method will yield a candidate for the final file."""

        raise NotImplementedError  # pragma: no cover

    def attempt_to_get_temporary_file(self, download_dir: FilePath) -> FilePath | None:
        """Attempt to get the name of the temporary file of the current download."""

        def get_temporary_file_candidates() -> list[str]:
            download_dir_entries = helper.directory.get_entries(download_dir)
            return [file for file in download_dir_entries if self.is_temporary_file(download_dir, file)]

        if self.uses_temporary_file:
            temporary_file_candidates = get_temporary_file_candidates()
            match len(temporary_file_candidates):
                case 0:  # It may be that the download has already finished, and so the temporary file may have been cleaned up.
                    self.temporary_file = None
                case 1:
                    file_path = os.path.join(download_dir, temporary_file_candidates[0])
                    self.temporary_file = FilePath(file_path)
                case _:
                    self.temporary_file = None
                    raise Exception("Multiple temporary files found. Not possible to determine which is for this download.")  # TODO: Update Exception type.
        return self.temporary_file

    def attempt_to_get_file(self, download_dir_entries_before_download: list[str], download_dir: FilePath) -> FilePath | None:
        """Attempt to get the file name of the current download."""

        if self.temporary_file_predicts_final_file and self.temporary_file is not None:
            file_candidate = self.get_temporary_file_without_extension()
            if helper.file.exists(file_candidate):
                self.file = file_candidate
                return self.file

        current_download_dir_entries = helper.directory.get_entries(download_dir)
        file_candidates = [file for file in current_download_dir_entries if file not in download_dir_entries_before_download]
        return FilePath(file_candidates[0]) if len(file_candidates) == 1 else None

        # TODO: Update flow and exception handling.
