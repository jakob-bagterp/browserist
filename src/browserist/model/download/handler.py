import os
from abc import ABC, abstractmethod
from pathlib import Path

from ... import helper_iteration
from ...browser.wait.until.download_file.exists import wait_until_download_file_exists
from ...browser.wait.until.download_file.size_does_not_increase import wait_until_download_file_size_does_not_increase
from ...exception.download import DownloadHandlerMultipleFinalFilesError, DownloadHandlerMultipleTemporaryFilesError
from ...helper.directory import get_entries as get_directory_entries
from ...helper.file import exists as file_exists
from ..browser.base.driver import BrowserDriver
from ..type.path import FilePath


class DownloadHandler(ABC):
    """Abstract class that contains the download handler methods for various browser types."""

    __slots__ = [
        "_browser_driver",
        "_download_dir",
        "_download_dir_entries_before_download",
        "_idle_download_timeout",
        "_temporary_file",
        "_final_file",
    ]

    def __init__(
        self,
        browser_driver: BrowserDriver,
        download_dir_entries_before_download: list[str],
        idle_download_timeout: float,
    ) -> None:
        self._browser_driver: BrowserDriver = browser_driver
        self._download_dir: FilePath = browser_driver.settings._download_dir
        self._download_dir_entries_before_download: list[str] = download_dir_entries_before_download
        self._idle_download_timeout: float = idle_download_timeout
        self._temporary_file: FilePath | None = None
        self._final_file: FilePath | None = None

    @property
    @abstractmethod
    def _uses_temporary_file(self) -> bool:
        """Configuration property to set if the browser uses temporary files for downloads."""

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def _temporary_file_predicts_final_file(self) -> bool:
        """Some browsers add a temporary file extension to the download file, making it easier to determine what the name of the final file is."""

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def _temporary_file_extension(self) -> str:
        """Property to define the temporary file extension used by the given browser.

        For example: `.download` for Safari, `.crdownload` for Chrome, `.part` for Firefox, etc."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def _is_preliminary_temporary_file(self, file_name: str) -> bool:
        """Some browsers may use transient preliminary download files, for example `.com.google.Chrome.1a2b3c` for Chrome, that evaporates quickly until a temporary file is created. Check whether a file name appears to be a preliminary temporary file for the specific browser."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def _is_temporary_file(self, file_name: str) -> bool:
        """If browsers use temporary download files, they all have different formats. Check whether a file name appears to be a temporary file for the specific browser."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def _get_temporary_file_from_expected_file(self, expected_file_name: str) -> str:
        """If a browser's temporary download file predicts the final file name – for instance by adding an extension – this method will yield a candidate for the name of the temporary file."""

        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def _get_temporary_file_without_extension(self) -> str:
        """If a browser's temporary download file predicts the final file name – for instance by adding an extension – this method will yield a candidate for the name of the final file."""

        raise NotImplementedError  # pragma: no cover

    def _as_download_dir_path(self, file_name: str) -> FilePath:
        """Get the path of a given file in the download directory."""

        return FilePath(os.path.join(self._download_dir, file_name))

    def _has_no_new_files_in_download_directory(self, download_dir_entries: list[str]) -> bool:
        number_of_current_download_dir_entries = len(download_dir_entries)
        number_of_download_dir_entries_before_download = len(self._download_dir_entries_before_download)
        return number_of_current_download_dir_entries <= number_of_download_dir_entries_before_download

    def _await_no_preliminary_temporary_file(self) -> None:
        """If the browser uses preliminary temporary files transiently before a temporary file is created, wait until any preliminary files has evaporated."""

        def has_any_new_preliminary_temporary_files() -> bool:
            download_dir_entries = get_directory_entries(self._download_dir)
            if self._has_no_new_files_in_download_directory(download_dir_entries):
                return False
            download_dir_entries_difference = [
                file for file in download_dir_entries if file not in self._download_dir_entries_before_download
            ]
            return any(self._is_preliminary_temporary_file(file) for file in download_dir_entries_difference)

        helper_iteration.retry.until_condition_is_false(
            self._browser_driver,
            func=has_any_new_preliminary_temporary_files,
            timeout=self._idle_download_timeout,
            func_uses_browser_driver=False,
        )

    def _attempt_to_get_temporary_file(self) -> FilePath | None:
        """Attempt to get the name of the temporary file of the current download."""

        def get_temporary_file_candidates() -> list[str]:
            download_dir_entries = get_directory_entries(self._download_dir)
            return [file for file in download_dir_entries if self._is_temporary_file(file)]

        if self._uses_temporary_file:
            temporary_file_candidates = get_temporary_file_candidates()
            match len(temporary_file_candidates):
                case 0:  # It may be that the download has already finished, and so the temporary file may have been cleaned up.
                    self._temporary_file = None
                case 1:
                    self._temporary_file = self._as_download_dir_path(temporary_file_candidates[0])
                case _:
                    self._temporary_file = None
                    raise DownloadHandlerMultipleTemporaryFilesError(temporary_file_candidates)
        return self._temporary_file

    def _attempt_to_get_final_file(self) -> FilePath | None:
        """Attempt to get the file name of the current download."""

        def get_final_file_candidates() -> list[str]:
            current_download_dir_entries = get_directory_entries(self._download_dir)
            return [
                file for file in current_download_dir_entries if file not in self._download_dir_entries_before_download
            ]

        def get_final_file_candidate() -> str | None:
            file_candidates = get_final_file_candidates()
            match len(file_candidates):
                case 0:
                    return None
                case 1:
                    return file_candidates[0]
                case _:
                    raise DownloadHandlerMultipleFinalFilesError(file_candidates)

        def quick_exit_is_possibly_and_final_file_is_already_downloaded() -> bool:
            if self._temporary_file_predicts_final_file and self._temporary_file is not None:
                file_candidate = self._get_temporary_file_without_extension()
                file_candidate_path = self._as_download_dir_path(file_candidate)
                if file_exists(file_candidate_path):
                    self._final_file = file_candidate_path
                    return True
            return False

        if quick_exit_is_possibly_and_final_file_is_already_downloaded():
            return self._final_file

        file_candidate = get_final_file_candidate()
        if file_candidate is None:
            self._final_file = None
            return self._final_file
        if self._is_temporary_file(
            file_candidate
        ):  # In esoteric cases where the temporary file has passed through earlier checks, the final file candidate may be a temporary file.
            if self._temporary_file_predicts_final_file and self._temporary_file is not None:
                file_candidate = self._get_temporary_file_without_extension()
            else:
                temporary_file = file_candidate
                wait_until_download_file_size_does_not_increase(
                    self._browser_driver, temporary_file, self._idle_download_timeout
                )
                file_candidate = get_final_file_candidate()
                if file_candidate is None:
                    self._final_file = None
                    return self._final_file
        self._final_file = self._as_download_dir_path(file_candidate)
        return self._final_file

    def _await_files_in_download_dir(self) -> None:
        """Ensure that the browser has a short moment to do file operations on the disk."""

        def has_files_in_download_dir(number_of_download_dir_entries_before_download: int) -> bool:
            """Watch for changes in the download directory, for instance until 0 files change to 1 file."""

            if number_of_download_dir_entries_before_download == 0:
                download_dir_entries = get_directory_entries(self._download_dir)
                return len(download_dir_entries) > number_of_download_dir_entries_before_download
            else:
                return True

        number_of_download_dir_entries_before_download = len(get_directory_entries(self._download_dir))
        helper_iteration.retry.until_condition_is_true(
            self._browser_driver,
            number_of_download_dir_entries_before_download,
            func=has_files_in_download_dir,
            timeout=self._idle_download_timeout,
            func_uses_browser_driver=False,
        )

    def wait_for_expected_file(self, expected_file_name: str) -> None:
        """Wait for the expected file to be downloaded. If not found, an exception is raised."""

        def quick_exit_is_possibly_with_confirmed_final_file_and_then_await_download(expected_file_name: str) -> bool:
            """If it's a small, fast download, the temporary file may only be short-lived, or maybe the final file is already ready, and so let's check for the final file first for quick return."""

            if file_exists(expected_file_path):
                wait_until_download_file_size_does_not_increase(
                    self._browser_driver, expected_file_name, self._idle_download_timeout
                )
                return True
            else:
                return False

        def temporary_file_yields_final_file_then_await_download(expected_file_name: str) -> bool:
            if self._temporary_file_predicts_final_file:
                expected_temporary_file_name = self._get_temporary_file_from_expected_file(expected_file_name)
                wait_until_download_file_size_does_not_increase(
                    self._browser_driver, expected_temporary_file_name, self._idle_download_timeout
                )
                wait_until_download_file_size_does_not_increase(
                    self._browser_driver, expected_file_name, self._idle_download_timeout
                )
                return True if file_exists(expected_file_path) else False
            else:
                return False

        def temporary_file_is_found_then_await_download_of_final_file(expected_file_name: str) -> bool:
            if not self._temporary_file_predicts_final_file:
                if self._attempt_to_get_temporary_file() and self._temporary_file is not None:
                    wait_until_download_file_size_does_not_increase(
                        self._browser_driver, self._temporary_file.name, self._idle_download_timeout
                    )
                wait_until_download_file_size_does_not_increase(
                    self._browser_driver, expected_file_name, self._idle_download_timeout
                )
                return True if file_exists(expected_file_path) else False
            else:
                return False

        self._await_files_in_download_dir()
        expected_file_path = self._as_download_dir_path(expected_file_name)
        if quick_exit_is_possibly_with_confirmed_final_file_and_then_await_download(expected_file_name):
            return
        # If no quick exit is possible, let's fall back to checking for the temporary and final files.
        self._await_no_preliminary_temporary_file()
        if temporary_file_yields_final_file_then_await_download(expected_file_name):
            return
        elif temporary_file_is_found_then_await_download_of_final_file(expected_file_name):
            return
        wait_until_download_file_exists(self._browser_driver, expected_file_name, self._idle_download_timeout)
        wait_until_download_file_size_does_not_increase(
            self._browser_driver, expected_file_name, self._idle_download_timeout
        )

    def await_and_get_final_file(self) -> Path:
        """Await the download to finish and return the file path."""

        self._await_files_in_download_dir()
        self._await_no_preliminary_temporary_file()
        self._attempt_to_get_temporary_file()
        if self._temporary_file is not None:
            wait_until_download_file_size_does_not_increase(
                self._browser_driver, self._temporary_file.name, self._idle_download_timeout
            )
        self._attempt_to_get_final_file()
        if self._final_file is not None:
            self.wait_for_expected_file(self._final_file)
        return self._final_file.path if self._final_file is not None else Path("")
