from typing import Generator

import pytest
from _config.browser_settings import default

from browserist import Browser

@pytest.fixture(scope = "session")
def browser_default_headless() -> Generator[Browser, None, None]:
    """Reuse a shared Browser in default, headless mode across tests so each test doesn't have to initialize a new Browser, which is slower."""

    with Browser(default.HEADLESS) as browser:
        yield browser
