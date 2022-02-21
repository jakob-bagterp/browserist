from browserist import BrowserSettings
from browserist import BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.OPERA,
)

HEADLESS = BrowserSettings(
    type=BrowserType.OPERA,
    headless=True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.OPERA,
    headless=True,
    disable_images=True
)
