import sys


def is_python_version(major: int, minor: int) -> bool:
    return major == sys.version_info.major and minor == sys.version_info.minor
