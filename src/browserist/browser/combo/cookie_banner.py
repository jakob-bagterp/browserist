import time

from ...constant import timeout
from ...model.browser.base.settings import BrowserSettings
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ..click.button import click_button
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.element_disappears import wait_until_element_disappears


def combo_cookie_banner(driver: object, settings: BrowserSettings, cookie_banner: CookieBannerSettings) -> None:
    # TODO: Incorporate timeout strategy and settings
    # TODO: Handle timeout.DEFAULT in alignment with timeout strategy and settings

    if cookie_banner.url is not None:
        open_url_if_not_current(driver, cookie_banner.url)
    if cookie_banner.has_loaded_wait_seconds is not None:
        time.sleep(cookie_banner.has_loaded_wait_seconds)
    if cookie_banner.has_loaded_xpath is not None:
        wait_for_element(driver, settings, cookie_banner.has_loaded_xpath, timeout.DEFAULT)
    click_button(driver, settings, cookie_banner.button_xpath, timeout.DEFAULT)
    if cookie_banner.has_disappeared_wait_seconds is not None:
        time.sleep(cookie_banner.has_disappeared_wait_seconds)
    else:
        time.sleep(timeout.VERY_SHORT)
    wait_until_element_disappears(driver, cookie_banner.button_xpath, timeout.DEFAULT)
