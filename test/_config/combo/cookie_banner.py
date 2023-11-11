from _mock_data.url import internal_url
from browserist import CookieBannerSettings

HAS_LOADED_XPATH = "//*[@id='cookie-banner']"

ACCEPT_BUTTON_XPATH = "//button[@id='accept-cookies']"

COOKIE_BANNER_SETTINGS_WITH_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    iframe_xpath="//iframe[@id='cookie-banner-iframe']",
    has_loaded_xpath=HAS_LOADED_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)

COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=HAS_LOADED_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)
