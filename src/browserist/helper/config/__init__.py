from selenium import webdriver
from ...model.browser import BrowserConfig, BrowserType

def set_webdriver(config: BrowserConfig) -> object:
    match(config.type):
        case BrowserType.CHROME:
            return webdriver.Chrome
        case BrowserType.FIREFOX:
            return webdriver.Firefox
