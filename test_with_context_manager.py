from src.browserist import Browser

with Browser() as browser:
    browser.open.url_if_not_current("https://www.dr.dk/")
