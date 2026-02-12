from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(type=BrowserType.SAFARI, check_connection=False)

HEADLESS = BrowserSettings(type=BrowserType.SAFARI, headless=True, check_connection=False)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.SAFARI, headless=True, disable_images=True, check_connection=False
)
