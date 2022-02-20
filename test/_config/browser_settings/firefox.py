from browserist import BrowserSettings
from browserist import BrowserType

DEFAULT = BrowserSettings(
    type = BrowserType.FIREFOX,
)

HEADLESS = BrowserSettings(
    type     = BrowserType.FIREFOX,
    headless = True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type           = BrowserType.FIREFOX,
    headless       = True,
    disable_images = True
)
