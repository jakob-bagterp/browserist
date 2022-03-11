from _helper import external_url

from browserist import CookieBannerSettings

DBA_ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[@id='onetrust-accept-btn-handler']",
    url=external_url.DBA_DK
)

GOOGLE_ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[2]",
    url=external_url.GOOGLE_COM
)
