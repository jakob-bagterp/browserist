import time

from src.browserist import Browser

with Browser() as browser:
    browser.open.new_tab()
    browser.open.new_tab("http://example.com")
    time.sleep(5)
