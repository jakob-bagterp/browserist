from abc import ABC, abstractmethod


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
    def is_temporary_file(self, file_name: str) -> bool:
        """If browsers use temporary download files, they all have different formats. Check whether a file name appears to be a temporary file for the specific browser."""

        raise NotImplementedError  # pragma: no cover
