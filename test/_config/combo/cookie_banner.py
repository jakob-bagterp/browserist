from _mock_data.url import internal_url

from browserist import CookieBannerSettings

COOKIE_BANNER_CONTAINER_XPATH = "//*[@id='cookie-banner']"

COOKIE_BANNER_IFRAME_XPATH = "//iframe[@id='cookie-banner-iframe']"

ACCEPT_BUTTON_XPATH = "//button[@id='accept-cookies']"

COOKIE_BANNER_SETTINGS_WITH_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    iframe_xpath=COOKIE_BANNER_IFRAME_XPATH,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)

COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
)

COOKIE_BANNER_SETTINGS_WITH_IFRAME_WITH_RETURN_BOOL_AND_SUCCESS_STATE = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    iframe_xpath=COOKIE_BANNER_IFRAME_XPATH,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
    return_bool=True,
)

COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME_WITH_RETURN_BOOL_AND_SUCCESS_STATE = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath=ACCEPT_BUTTON_XPATH,
    return_bool=True,
)

COOKIE_BANNER_SETTINGS_WITH_IFRAME_WITH_RETURN_BOOL_AND_ERROR_STATE = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    iframe_xpath=COOKIE_BANNER_IFRAME_XPATH,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath="//no/button",
    return_bool=True,
)

COOKIE_BANNER_SETTINGS_WITHOUT_IFRAME_WITH_RETURN_BOOL_AND_ERROR_STATE = CookieBannerSettings(
    url=internal_url.COOKIE_BANNER_WITHOUT_IFRAME,
    has_loaded_xpath=COOKIE_BANNER_CONTAINER_XPATH,
    button_xpath="//no/button",
    return_bool=True,
)
