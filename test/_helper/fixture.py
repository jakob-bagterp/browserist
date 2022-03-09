from typing import Generator

import pytest
from _config.browser_settings import default
from _mock_data.window_handles import (WINDOW_HANDLE_1_ID, WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_2_ID,
                                       WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_3_ID, WINDOW_HANDLE_3_NAME)

from browserist import Browser
from browserist.model.window.controller import WindowHandleController
from browserist.model.window.handle import WindowHandle


@pytest.fixture(scope="session")
def browser_default_headless() -> Generator[Browser, None, None]:
    """Reuse a shared Browser in default, headless mode across tests so each test doesn't have to initialize a new Browser, which is slower."""

    with Browser(default.HEADLESS) as browser:
        yield browser


@pytest.fixture(scope="session")
def browser_default() -> Generator[Browser, None, None]:
    """Reuse a shared Browser in default, headless mode across tests so each test doesn't have to initialize a new Browser, which is slower."""

    with Browser(default.DEFAULT) as browser:
        yield browser


@pytest.fixture(scope="module")
def window_handle_controller() -> WindowHandleController:
    with Browser(default.HEADLESS) as browser:
        window_handle_controller = WindowHandleController(browser.driver)
        window_handle_controller._window_handles = [
            WindowHandle(WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_1_ID),
            WindowHandle(WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_2_ID),
            WindowHandle(WINDOW_HANDLE_3_NAME, WINDOW_HANDLE_3_ID),
        ]
        window_handle_controller._counter = len(window_handle_controller._window_handles)
        return window_handle_controller
