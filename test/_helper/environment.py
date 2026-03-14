import os

import pytest


def is_github_actions() -> bool:
    return os.getenv("GITHUB_ACTIONS") == "true"


def skip_if_github_actions(
    reason: str = "Test skipped in GitHub Actions as it requires a local/non-headless browser environment.",
) -> pytest.MarkDecorator:
    return pytest.mark.skipif(is_github_actions(), reason=reason)


SKIP_TIMING_PERFORMANCE_TESTS = "Test skipped as it evaluates timing and/or network performance indirectly, and so it likely fails on GitHub Actions. Only run on a local machine."

FAILS_ON_GITHUB_ACTIONS = (
    "Test skipped as it (most often) fails on GitHub Actions, but not when running on a local machine."
)
