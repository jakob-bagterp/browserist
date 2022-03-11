from copy import deepcopy
from typing import Generator

import pytest
from _config.browser_settings import default
from _mock_data.window_handles import WINDOW_HANDLES
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.model.window.controller import WindowHandleController


@pytest.fixture(scope="session")
def browser_default_headless() -> Generator[Browser, None, None]:
    """Reuse a shared Browser in default, headless mode across tests so each test doesn't have to initialize a new Browser, which is slower."""

    with Browser(default.HEADLESS) as browser:
        yield browser


@pytest.fixture(scope="function")
def browser_default_headless_scope_function() -> Generator[Browser, None, None]:
    """Reuse a shared Browser in default, headless mode across tests so each test doesn't have to initialize a new Browser, which is slower."""

    with Browser(default.HEADLESS) as browser:
        yield browser


@pytest.fixture(scope="session")
def browser_default() -> Generator[Browser, None, None]:
    """Reuse a shared Browser in default, headless mode across tests so each test doesn't have to initialize a new Browser, which is slower."""

    with Browser(default.DEFAULT) as browser:
        yield browser


@pytest.fixture(scope="function")
def browser_headless_screenshot(tmpdir: local) -> Generator[Browser, None, None]:
    """Reuse a shared Browser in headless mode with special temporary directory configuration for screenshots."""

    browser_settings = BrowserSettings(
        headless=True,
        screenshot_dir=str(tmpdir)
    )
    with Browser(browser_settings) as browser:
        yield browser


@pytest.fixture(scope="function")
def window_handle_controller() -> WindowHandleController:
    with Browser(default.HEADLESS) as browser:
        window_handle_controller = WindowHandleController(browser.driver)
        window_handle_controller._window_handles = deepcopy(WINDOW_HANDLES)
        window_handle_controller._counter = len(window_handle_controller._window_handles)
        return window_handle_controller
