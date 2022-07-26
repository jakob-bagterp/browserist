from _config.timeout_settings import DEFAULT_NO_TIMEOUT

from browserist import BrowserSettings

DEFAULT = BrowserSettings(
    timeout=DEFAULT_NO_TIMEOUT
)

HEADLESS = BrowserSettings(
    headless=True,
    timeout=DEFAULT_NO_TIMEOUT
)

DISABLE_IMAGES = BrowserSettings(
    disable_images=True,
    timeout=DEFAULT_NO_TIMEOUT
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    headless=True,
    disable_images=True,
    timeout=DEFAULT_NO_TIMEOUT
)
