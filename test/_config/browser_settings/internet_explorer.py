from _config.timeout_settings import DEFAULT_NO_TIMEOUT

from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.INTERNET_EXPLORER,
    timeout=DEFAULT_NO_TIMEOUT
)

HEADLESS = BrowserSettings(
    type=BrowserType.INTERNET_EXPLORER,
    headless=True,
    timeout=DEFAULT_NO_TIMEOUT
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.INTERNET_EXPLORER,
    headless=True,
    disable_images=True,
    timeout=DEFAULT_NO_TIMEOUT
)
