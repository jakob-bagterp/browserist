from _config import timeout_settings

from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.OPERA,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

HEADLESS = BrowserSettings(
    type=BrowserType.OPERA,
    headless=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.OPERA,
    headless=True,
    disable_images=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)
