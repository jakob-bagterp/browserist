import contextlib
import subprocess

import pytest

from browserist.helper import operating_system


def pytest_session_cleanup(session: pytest.Session, exitstatus: int | pytest.ExitCode) -> None:
    """If a session hangs due to background threads or file locks, this forces the Python process to exit immediately with the correct status, including skipping thread joins and garbage collection of orphaned browser processes."""

    def kill_process(process: str) -> None:
        subprocess.run(
            ["taskkill", "/F", "/IM", process, "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
        )

    # Prevent pytest-xdist workers from executing this hook, as it may cause issues:
    if hasattr(session.config, "workerinput"):
        return

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
            with contextlib.suppress(Exception):
                kill_process(process)
