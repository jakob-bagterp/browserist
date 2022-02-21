from browserist import BrowserSettings
from browserist import BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.EDGE,
)

HEADLESS = BrowserSettings(
    type=BrowserType.EDGE,
    headless=True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.EDGE,
    headless=True,
    disable_images=True
)
