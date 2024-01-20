from ... import helper, helper_download
from .handler import DownloadHandler


class SafariDownloadHandler(DownloadHandler):
    @property
    def _uses_temporary_file(self) -> bool:
        return True

    @property
    def _temporary_file_predicts_final_file(self) -> bool:
        return True

    @property
    def _temporary_file_extension(self) -> str:
        return ".download"

    def _is_preliminary_temporary_file(self, file_name: str) -> bool:
        return False  # Not supported by Safari.

    def _is_temporary_file(self, file_name: str) -> bool:
        """When Safari starts a download, it uses `.download` as extension for temporary files.

        For example, it creates the temporary file `file.zip.download` until fully downloaded and then renames it to `file.zip`."""

        return file_name.endswith(self._temporary_file_extension) and helper.file.is_file(self._download_dir, file_name)

    def _get_temporary_file_from_expected_file(self, expected_file_name: str) -> str:
        return helper_download.add_file_extension(expected_file_name, self._temporary_file_extension)

    def _get_temporary_file_without_extension(self) -> str:
        if self._temporary_file is not None:
            return helper_download.remove_file_extension(self._temporary_file.name, self._temporary_file_extension)
        else:
            return ""
