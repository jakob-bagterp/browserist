from copy import deepcopy

import pytest
from _config.browser_settings import default
from _mock_data.window_handles import WINDOW_HANDLES

from browserist import Browser
from browserist.model.window.controller import WindowHandleController


@pytest.fixture(scope="function")
def window_handle_controller() -> WindowHandleController:
    with Browser(default.HEADLESS) as browser:
        window_handle_controller = WindowHandleController(browser.driver)
        window_handle_controller._window_handles = deepcopy(WINDOW_HANDLES)
        window_handle_controller._counter = len(window_handle_controller._window_handles)
        return window_handle_controller
