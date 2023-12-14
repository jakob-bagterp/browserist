from ... import helper
from ..type.path import FilePath
from .handler import DownloadHandler


class FirefoxDownloadHandler(DownloadHandler):
    @property
    def uses_temporary_file(self) -> bool:
        return True

    @property
    def temporary_file_predicts_final_file(self) -> bool:
        return False

    @property
    def temporary_file_extension(self) -> str:
        return ".part"

    def is_temporary_file(self, download_dir: FilePath, file_name: str) -> bool:
        """When Firefox starts a download, it uses `.part` as extension for temporary files.

        For example, it creates the temporary file with a random name `a1b2.zip.part` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(self.temporary_file_extension) and helper.file.is_file(download_dir, file_name)

    def get_temporary_file_without_extension(self) -> FilePath | None:
        return None  # Not supported by Firefox.
