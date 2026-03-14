from pathlib import Path

import pytest
from _helper.environment import is_github_actions


def pytest_ignore_collection(collection_path: Path, config: pytest.Config) -> bool:
    if is_github_actions():
        ignored_files = [
            "test/browser/input/select_1_test.py",
            "test/browser/viewport/get/height_non_headless_1_test.py",
            "test/browser/viewport/get/height_non_headless_2_test.py",
            "test/browser/viewport/get/size_non_headless_1_test.py",
            "test/browser/viewport/get/size_non_headless_2_test.py",
            "test/browser/viewport/get/width_non_headless_1_test.py",
            "test/browser/viewport/get/width_non_headless_2_test.py",
            "test/browser/viewport/set/size_by_device_non_headless_test.py",
        ]

        if any(str(collection_path).endswith(path) for path in ignored_files):
            return True

    return False
