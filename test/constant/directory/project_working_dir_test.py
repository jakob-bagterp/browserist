from pathlib import Path

from browserist import constant


def test_project_working_dir() -> None:
    assert constant.directory.PROJECT_WORKING_DIR.is_dir() is True
    assert constant.directory.PROJECT_WORKING_DIR == Path(__file__).parent.parent.parent.parent
