from browserist import BrowserSettings
from browserist import BrowserType

DEFAULT = BrowserSettings(
    type = BrowserType.INTERNET_EXPLORER,
)

HEADLESS = BrowserSettings(
    type     = BrowserType.INTERNET_EXPLORER,
    headless = True
)

HEADLESS_AND_DISABLE_IMAGES = BrowserSettings(
    type           = BrowserType.INTERNET_EXPLORER,
    headless       = True,
    disable_images = True
)
