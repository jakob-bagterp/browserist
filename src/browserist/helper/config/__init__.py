__all__ = ["chrome", "firefox"]

from . import chrome, firefox

from selenium import webdriver
from ...model.browser import BrowserSettings, BrowserType

def set_webdriver(settings: BrowserSettings) -> object:
    match(settings.type):
        case BrowserType.CHROME:
            return webdriver.Chrome
        case BrowserType.FIREFOX:
            return webdriver.Firefox
