from _config import timeout_settings

from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.SAFARI,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

HEADLESS = BrowserSettings(
    type=BrowserType.SAFARI,
    headless=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.SAFARI,
    headless=True,
    disable_images=True,
    timeout=timeout_settings.DEFAULT_CONTINUE
)
