import time

from ... import constant
from ...model.browser.base.driver import BrowserDriver
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ..click.button import click_button
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.element_disappears import wait_until_element_disappears


def combo_cookie_banner(browser_driver: BrowserDriver, cookie_banner: CookieBannerSettings, timeout: int) -> None:
    # TODO: Incorporate timeout strategy and settings

    if cookie_banner.url is not None:
        open_url_if_not_current(browser_driver, cookie_banner.url)
    if cookie_banner.has_loaded_wait_seconds is not None:
        time.sleep(cookie_banner.has_loaded_wait_seconds)
    if cookie_banner.has_loaded_xpath is not None:
        wait_for_element(browser_driver, cookie_banner.has_loaded_xpath, timeout)
    click_button(browser_driver, cookie_banner.button_xpath, timeout)
    if cookie_banner.has_disappeared_wait_seconds is not None:
        time.sleep(cookie_banner.has_disappeared_wait_seconds)
    else:
        time.sleep(constant.timeout.VERY_SHORT)
    wait_until_element_disappears(browser_driver, cookie_banner.button_xpath, timeout)
