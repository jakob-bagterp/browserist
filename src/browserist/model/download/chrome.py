from ... import helper
from ..type.path import FilePath
from .handler import DownloadHandler


class ChromeDownloadHandler(DownloadHandler):
    @property
    def _uses_temporary_file(self) -> bool:
        return True

    @property
    def _temporary_file_predicts_final_file(self) -> bool:
        return True

    @property
    def _temporary_file_extension(self) -> str:
        return ".crdownload"

    def _is_temporary_file(self, file_name: str) -> bool:
        """When Chrome starts a download, it uses `.crdownload` as extension for temporary files.

        For example, it creates the temporary file `file.zip.crdownload` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(self._temporary_file_extension) and helper.file.is_file(self._download_dir, file_name)

    def _get_temporary_file_without_extension(self) -> FilePath | None:
        if self._temporary_file_predicts_final_file and self._temporary_file is not None:
            file_path = self._temporary_file.rstrip(self._temporary_file_extension)
            return FilePath(file_path)
        else:
            return None
