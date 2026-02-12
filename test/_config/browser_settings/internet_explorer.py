from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(type=BrowserType.INTERNET_EXPLORER, check_connection=False)

HEADLESS = BrowserSettings(type=BrowserType.INTERNET_EXPLORER, headless=True, check_connection=False)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.INTERNET_EXPLORER, headless=True, disable_images=True, check_connection=False
)
