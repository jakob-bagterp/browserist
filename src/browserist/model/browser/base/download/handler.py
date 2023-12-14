import os
from abc import ABC, abstractmethod

from ..... import helper
from ....type.path import FilePath


class DownloadHandler(ABC):
    """Abstract class that contains the download handler methods for various browser types."""

    @property
    @abstractmethod
    def uses_temporary_file(self) -> bool:
        """Configuration property to set if the browser uses temporary files for downloads."""

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def temporary_file_extension(self) -> str:
        """Property to define the temporary file extension used by the given browser.

        For example: `download` for Safari, `crdownload` for Chrome, `part` for Firefox, etc."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def is_temporary_file(self, download_dir: FilePath, file_name: str) -> bool:
        """If browsers use temporary download files, they all have different formats. Check whether a file name appears to be a temporary file for the specific browser."""

        raise NotImplementedError  # pragma: no cover

    def get_temporary_file_name(self, download_dir: FilePath) -> FilePath | None:
        """Attempt to get the name of the temporary file of the current download."""

        if self.uses_temporary_file:
            download_dir_entries = helper.directory.get_entries(download_dir)
            temporary_files = [file for file in download_dir_entries if self.is_temporary_file(download_dir, file)]
            match len(temporary_files):
                case 0:
                    raise Exception("No temporary file found.")
                    # TODO: Update Exception type.
                case 1:
                    file_path = os.path.join(download_dir, temporary_files[0])
                    return FilePath(file_path)
                case _:
                    raise Exception("Multiple temporary files found.")
                    # TODO: Update Exception type.
        return None
