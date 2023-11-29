from collections.abc import Generator

import pytest
from _config import timeout_settings
from _config.browser_settings import default
from py.path import local

from browserist import Browser, BrowserSettings
from browserist.model.browser.base.type import BrowserType

# Reuse a shared Browser whether it's in default or headless mode across tests
# so each test doesn't have to initialize a new Browser, which is slower.


@pytest.fixture(scope="session")
def browser_default() -> Generator[Browser, None, None]:
    with Browser(default.DEFAULT) as browser:
        yield browser


@pytest.fixture(scope="session")
def browser_default_headless() -> Generator[Browser, None, None]:
    with Browser(default.HEADLESS) as browser:
        yield browser


@pytest.fixture(scope="session")
def browser_default_headless_disable_images() -> Generator[Browser, None, None]:
    with Browser(default.HEADLESS_AND_DISABLE_IMAGES) as browser:
        yield browser


@pytest.fixture(scope="session")
def browser_default_headless_timeout_strategy_continue() -> Generator[Browser, None, None]:
    browser_settings = BrowserSettings(
        headless=True,
        disable_images=True,
        timeout=timeout_settings.DEFAULT_CONTINUE
    )
    with Browser(browser_settings) as browser:
        yield browser


@pytest.fixture(scope="session")
def browser_default_headless_timeout_strategy_stop() -> Generator[Browser, None, None]:
    browser_settings = BrowserSettings(
        headless=True,
        disable_images=True,
        timeout=timeout_settings.DEFAULT_STOP
    )
    with Browser(browser_settings) as browser:
        yield browser


@pytest.fixture(scope="function")
def browser_default_headless_scope_function() -> Generator[Browser, None, None]:
    with Browser(default.HEADLESS) as browser:
        yield browser


@pytest.fixture(scope="function")
def browser_default_headless_screenshot(tmpdir: local) -> Generator[Browser, None, None]:
    browser_settings = BrowserSettings(
        headless=True,
        screenshot_dir=str(tmpdir)
    )
    with Browser(browser_settings) as browser:
        yield browser


@pytest.fixture(scope="function")
def browser_firefox_headless_screenshot(tmpdir: local) -> Generator[Browser, None, None]:
    browser_settings = BrowserSettings(
        type=BrowserType.FIREFOX,
        headless=True,
        screenshot_dir=str(tmpdir)
    )
    with Browser(browser_settings) as browser:
        yield browser
