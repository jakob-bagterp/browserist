import sys


def is_macos() -> bool:
    return sys.platform.startswith("darwin")


def is_windows() -> bool:
    return sys.platform.startswith("win32")
