import time

from ... import constant
from ...model.combo_settings.cookie_banner import CookieBannerSettings
from ...model.driver_methods import DriverMethods
from ..click.button import click_button
from ..open.url_if_not_current import open_url_if_not_current
from ..wait.for_element import wait_for_element
from ..wait.until.element_disappears import wait_until_element_disappears


def combo_cookie_banner(driver_method: DriverMethods, cookie_banner: CookieBannerSettings, timeout: int) -> None:
    if cookie_banner.url is not None and driver_method._timeout_should_continue():
        open_url_if_not_current(driver_method._browser_driver, cookie_banner.url)
    if cookie_banner.has_loaded_wait_seconds is not None:
        time.sleep(cookie_banner.has_loaded_wait_seconds)
    if cookie_banner.has_loaded_xpath is not None and driver_method._timeout_should_continue():
        wait_for_element(driver_method._browser_driver, cookie_banner.has_loaded_xpath, timeout)
    if driver_method._timeout_should_continue():
        click_button(driver_method._browser_driver, cookie_banner.button_xpath, timeout)
    if cookie_banner.has_disappeared_wait_seconds is not None:
        time.sleep(cookie_banner.has_disappeared_wait_seconds)
    else:
        time.sleep(constant.timeout.VERY_SHORT)
    if driver_method._timeout_should_continue():
        wait_until_element_disappears(driver_method._browser_driver, cookie_banner.button_xpath, timeout)
