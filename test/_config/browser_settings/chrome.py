from browserist import BrowserSettings
from browserist import BrowserType

DEFAULT = BrowserSettings(
    type=BrowserType.CHROME,
)

HEADLESS = BrowserSettings(
    type=BrowserType.CHROME,
    headless=True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type=BrowserType.CHROME,
    headless=True,
    disable_images=True
)
