from _config.browser_settings import default

from browserist import Browser


def test_is_not_singleton() -> None:
    with Browser(default.HEADLESS) as browser_1:
        with Browser(default.HEADLESS) as browser_2:
            assert browser_1 is not browser_2
