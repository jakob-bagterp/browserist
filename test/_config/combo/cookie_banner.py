from _mock_data.url import internal_url

from browserist import CookieBannerSettings

COOKIE_BANNER_CONTAINER_XPATH = "//*[@id='cookie-banner']"

ACCEPT_BUTTON_XPATH = "//button[@id='accept-cookies']"

COOKIE_BANNER_SETTINGS_WITH_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    iframe_xpath="//iframe[@id='cookie-banner-iframe']",
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)

COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)

COOKIE_BANNER_SETTINGS_WITH_RETURN_BOOL_AND_SUCCESS_STATE = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
    return_bool=True,
)

COOKIE_BANNER_SETTINGS_WITH_RETURN_BOOL_AND_ERROR_STATE = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath="//no/button",
    return_bool=True,
)
