from browserist import BrowserSettings, BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.SAFARI
)

HEADLESS = BrowserSettings(
    type=BrowserType.SAFARI,
    headless=True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.SAFARI,
    headless=True,
    disable_images=True
)
