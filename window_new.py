import time

from src.browserist import Browser

with Browser() as browser:
    browser.open.new_tab()
    time.sleep(2)
    browser.open.new_tab("http://example.com")
    time.sleep(2)
    browser.open.new_window()
    time.sleep(2)
    browser.open.new_window("http://example.com")
    time.sleep(2)
    browser.window.close()
    time.sleep(2)
