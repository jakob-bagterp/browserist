import os
import platform

import pytest


def pytest_sessionfinish(session: pytest.Session, exitstatus: int | pytest.ExitCode) -> None:
    """
    Diagnostic hook: If Windows hangs due to background threads or file locks,
    this forces the Python process to exit immediately with the correct status.
    """
    if platform.system() == "Windows":
        # Force the OS to kill the process, skipping thread joins and garbage collection
        # Cast exitstatus to int in case it is passed as a pytest.ExitCode enum
        os._exit(int(exitstatus))
