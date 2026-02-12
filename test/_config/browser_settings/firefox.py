from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(type=BrowserType.FIREFOX, check_connection=False)

HEADLESS = BrowserSettings(type=BrowserType.FIREFOX, headless=True, check_connection=False)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.FIREFOX, headless=True, disable_images=True, check_connection=False
)
