import os

import pytest


def is_github_actions() -> bool:
    return os.getenv("GITHUB_ACTIONS") == "true"


def skip_if_github_actions(
    reason: str = "Test skipped in GitHub Actions as it requires a local/non-headless browser environment.",
) -> pytest.MarkDecorator:
    return pytest.mark.skipif(is_github_actions(), reason=reason)
