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
    window_handles = browser.window.handle.all()
    print(browser.window.handle.count(), window_handles)
    print(browser.window.handle.all())
    time.sleep(1)
    browser.window.close()
    window_handles = browser.window.handle.all()
    print(browser.window.handle.count(), window_handles)
    time.sleep(1)
