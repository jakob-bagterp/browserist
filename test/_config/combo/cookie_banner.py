from _helper import external_url

from browserist import CookieBannerSettings

DBA_ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[@id='onetrust-accept-btn-handler']",
    url=external_url.DBA_DK
)
