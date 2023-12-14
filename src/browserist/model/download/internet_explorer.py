from ... import helper
from ..type.path import FilePath
from .handler import DownloadHandler


class InternetExplorerDownloadHandler(DownloadHandler):
    @property
    def uses_temporary_file(self) -> bool:
        return True

    @property
    def temporary_file_predicts_final_file(self) -> bool:
        return True

        # TODO: To be verified.

    @property
    def temporary_file_extension(self) -> str:
        return ".part"

        # TODO: To be verified.

    def is_temporary_file(self, download_dir: FilePath, file_name: str) -> bool:
        """TODO: To be verified."""

        return file_name.endswith(self.temporary_file_extension) and helper.file.is_file(download_dir, file_name)

        # TODO: To be verified.

    def get_temporary_file_without_extension(self) -> FilePath | None:
        if self.temporary_file_predicts_final_file and self.temporary_file is not None:
            file_path = self.temporary_file.rstrip(self.temporary_file_extension)
            return FilePath(file_path)
        else:
            return None

        # TODO: To be verified.
