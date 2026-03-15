import os
import subprocess

import pytest

from browserist.helper import operating_system


def pytest_session_cleanup_for_windows(session: pytest.Session, exitstatus: int | pytest.ExitCode) -> None:
    """If Windows hangs due to background threads or file locks, this forces the Python process to exit immediately with the correct status, including skipping thread joins and garbage collection of browser processes."""

    def kill_process(process: str) -> None:
        subprocess.run(
            ["taskkill", "/F", "/IM", process, "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
        )

    if operating_system.is_windows():
        browser_processes = [
            "chromedriver.exe",
            "chrome.exe",
            "msedgedriver.exe",
            "msedge.exe",
            "geckodriver.exe",
            "firefox.exe",
        ]
        for process in browser_processes:
            kill_process(process)

        os._exit(int(exitstatus))
