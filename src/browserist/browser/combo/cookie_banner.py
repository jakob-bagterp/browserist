import time

from ...constant import timeout
from ...exception.cookie_banner import CookieBannerException
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ..click.button import click_button
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until_element_disappears import wait_until_element_disappears


def combo_cookie_banner(driver: object, settings: CookieBannerSettings) -> None:
    try:
        if settings.url is not None:
            open_url_if_not_current(driver, settings.url)
        if settings.has_loaded_wait_seconds is not None:
            time.sleep(settings.has_loaded_wait_seconds)
        if settings.has_loaded_xpath is not None:
            wait_for_element(driver, settings.has_loaded_xpath)
        click_button(driver, settings.button_xpath)
        if settings.has_disappeared_wait_seconds is not None:
            time.sleep(settings.has_disappeared_wait_seconds)
        else:
            time.sleep(timeout.VERY_SHORT)
        wait_until_element_disappears(driver, settings.button_xpath)
    except Exception:
        raise CookieBannerException() from Exception
