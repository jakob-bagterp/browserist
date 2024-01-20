from ... import helper, helper_download
from .handler import DownloadHandler


class InternetExplorerDownloadHandler(DownloadHandler):
    @property
    def _uses_temporary_file(self) -> bool:
        return True

    @property
    def _temporary_file_predicts_final_file(self) -> bool:
        return True

        # TODO: To be verified.

    @property
    def _temporary_file_extension(self) -> str:
        return ".part"

        # TODO: To be verified.

    def _is_preliminary_temporary_file(self, file_name: str) -> bool:
        return False  # Not supported by Internet Explorer.

        # TODO: To be verified.

    def _is_temporary_file(self, file_name: str) -> bool:
        """TODO: To be verified."""

        return file_name.endswith(self._temporary_file_extension) and helper.file.is_file(self._download_dir, file_name)

        # TODO: To be verified.

    def _get_temporary_file_from_expected_file(self, expected_file_name: str) -> str:
        return helper_download.add_file_extension(expected_file_name, self._temporary_file_extension)

        # TODO: To be verified.

    def _get_temporary_file_without_extension(self) -> str:
        if self._temporary_file is not None:
            return helper_download.remove_file_extension(self._temporary_file.name, self._temporary_file_extension)
        else:
            return ""

        # TODO: To be verified.
