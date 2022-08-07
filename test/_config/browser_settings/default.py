from _config import timeout_settings

from browserist import BrowserSettings

DEFAULT = BrowserSettings(
    timeout=timeout_settings.DEFAULT_CONTINUE
)

HEADLESS = BrowserSettings(
    headless=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

DISABLE_IMAGES = BrowserSettings(
    disable_images=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    headless=True,
    disable_images=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)
