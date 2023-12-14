from ... import helper
from ..type.path import FilePath
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

    def _is_temporary_file(self, file_name: str) -> bool:
        """TODO: To be verified."""

        return file_name.endswith(self._temporary_file_extension) and helper.file.is_file(self._download_dir, file_name)

        # TODO: To be verified.

    def _get_temporary_file_without_extension(self) -> FilePath | None:
        if self._temporary_file_predicts_final_file and self._temporary_file is not None:
            file_path = self._temporary_file.rstrip(self._temporary_file_extension)
            return FilePath(file_path)
        else:
            return None

        # TODO: To be verified.
