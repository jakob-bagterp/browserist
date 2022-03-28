from _helper.url import external_url

from browserist import CookieBannerSettings
from browserist.constant import timeout

DBA_ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[@id='onetrust-accept-btn-handler']",
    url=external_url.DBA_DK,
    has_disappeared_wait_seconds=timeout.VERY_SHORT,
    has_loaded_wait_seconds=timeout.VERY_SHORT,
    has_loaded_xpath="//button[@id='onetrust-accept-btn-handler']"
)

GOOGLE_ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[2]",
    url=external_url.GOOGLE_COM
)

JYLLANDSPOSTEN_ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']",
    url=external_url.JYLLANDSPOSTEN_DK
)
