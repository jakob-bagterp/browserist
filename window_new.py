import time

from src.browserist import Browser

with Browser() as browser:
    browser.window.open.new_tab()
    time.sleep(2)
    browser.window.open.new_tab("http://example.com")
    time.sleep(2)
    browser.window.open.new()
    time.sleep(2)
    browser.window.open.new("http://example.com")
    window_handles = browser.driver.window_handles
    print(len(window_handles), window_handles)
    time.sleep(2)
    browser.window.close()
    window_handles = browser.driver.window_handles
    print(len(window_handles), window_handles)
    time.sleep(2)
