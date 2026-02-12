from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(type=BrowserType.CHROME, check_connection=False)

HEADLESS = BrowserSettings(type=BrowserType.CHROME, headless=True, check_connection=False)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.CHROME, headless=True, disable_images=True, check_connection=False
)
