from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(type=BrowserType.EDGE)

HEADLESS = BrowserSettings(type=BrowserType.EDGE, headless=True, check_connection=False)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.EDGE, headless=True, disable_images=True, check_connection=False
)
