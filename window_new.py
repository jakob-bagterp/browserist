import time

from src.browserist import Browser

with Browser() as browser:
    browser.window.open.new_tab()
    time.sleep(1)
    browser.window.open.new_tab("http://example.com")
    time.sleep(1)
    browser.window.open.new()
    time.sleep(1)
    browser.window.open.new("http://example.com")
    window_handles = browser.window.get.all_handles()
    print(browser.window.get.count_handles(), window_handles)
    print(browser.window.get.current_handle())
    time.sleep(1)
    browser.window.close()
    window_handles = browser.window.get.all_handles()
    print(browser.window.get.count_handles(), window_handles)
    time.sleep(1)
