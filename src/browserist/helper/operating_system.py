import sys


def is_linux() -> bool:
    return sys.platform.startswith("linux")


def is_macos() -> bool:
    return sys.platform.startswith("darwin")


def is_windows() -> bool:
    return sys.platform.startswith("win32")
