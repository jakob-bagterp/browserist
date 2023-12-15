from ... import helper
from .handler import DownloadHandler


class FirefoxDownloadHandler(DownloadHandler):
    @property
    def _uses_temporary_file(self) -> bool:
        return True

    @property
    def _temporary_file_predicts_final_file(self) -> bool:
        return False

    @property
    def _temporary_file_extension(self) -> str:
        return ".part"

    def _is_temporary_file(self, file_name: str) -> bool:
        """When Firefox starts a download, it uses `.part` as extension for temporary files.

        For example, it creates the temporary file with a random name `a1b2.zip.part` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(self._temporary_file_extension) and helper.file.is_file(self._download_dir, file_name)

    def _get_temporary_file_from_expected_file(self, expected_file_name: str) -> str:
        return ""  # Not supported by Firefox.

    def _get_temporary_file_without_extension(self) -> str:
        return ""  # Not supported by Firefox.
