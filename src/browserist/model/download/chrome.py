from ... import helper, helper_download
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

    def _is_preliminary_temporary_file(self, file_name: str) -> bool:
        """When Chrome starts a download, it may create a transient preliminary temporary file, for example `.com.google.Chrome.1a2b3c`, that evaporates quickly until a temporary file is created."""

        return file_name.startswith(".com.google.Chrome") and helper.file.is_file(self._download_dir, file_name)

    def _is_temporary_file(self, file_name: str) -> bool:
        """When Chrome starts a download, it uses `.crdownload` as extension for temporary files.

        For example, it creates the temporary file `file.zip.crdownload` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(self._temporary_file_extension) and helper.file.is_file(self._download_dir, file_name)

    def _get_temporary_file_from_expected_file(self, expected_file_name: str) -> str:
        return helper_download.add_file_extension(expected_file_name, self._temporary_file_extension)

    def _get_temporary_file_without_extension(self) -> str:
        if self._temporary_file is not None:
            return helper_download.remove_file_extension(self._temporary_file.name, self._temporary_file_extension)
        else:
            return ""
