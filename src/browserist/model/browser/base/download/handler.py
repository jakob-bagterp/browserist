from abc import ABC, abstractmethod


class DownloadHandler(ABC):
    """Abstract class that contains the download handler methods for various browser types."""

    @property
    @abstractmethod
    def uses_temp_file(self) -> bool:
        """Configuration to check if the browser uses a temporary file for download."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def is_temp_file(self, file_name: str) -> bool:
        """If browsers use temporary download files, they all have different formats. Check whether a file name appears to be a temporary file for the specific browser."""

        raise NotImplementedError  # pragma: no cover
