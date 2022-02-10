import time
from ..click.button import click_button
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.until_element_disappears import wait_until_element_disappears
from ..wait.for_element import wait_for_element
from ...exception.cookie_banner import CookieBannerException
from ...model.combo_settings.cookie_banner import CookieBannerSettings

def combo_cookie_banner(driver: object, settings: CookieBannerSettings) -> None:
    try:
        if settings.url is not None:
            open_url_if_not_current(driver, settings.url)
        time.sleep(settings.has_loaded_wait_seconds)
        if settings.has_loaded_xpath is not None:
            wait_for_element(driver, settings.has_loaded_xpath)
        click_button(driver, settings.button_xpath)
        time.sleep(settings.has_disappeared_wait_seconds)
        wait_until_element_disappears(driver, settings.button_xpath)
    except Exception:
        raise CookieBannerException() from Exception
