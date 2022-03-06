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
    print(browser.window.handle.all())
    time.sleep(1)

with Browser() as browser:
    browser.open.url("http://example.com")
    url_1 = browser.get.url.current()
    tab_handle_1 = browser.window.handle.current()
    number_of_tab_handles_1 = browser.window.handle.count()
    time.sleep(1)

    browser.window.open.new_tab("http://google.com")
    url_2 = browser.get.url.current()
    tab_handle_2 = browser.window.handle.current()
    number_of_tab_handles_2 = browser.window.handle.count()
    time.sleep(1)

    print(url_1, url_2)
    print(browser.window.handle.all())
    print(tab_handle_1, tab_handle_2)
    print(number_of_tab_handles_1, number_of_tab_handles_2)

    assert url_1 != url_2
    assert tab_handle_1 != tab_handle_2
    assert number_of_tab_handles_1 != number_of_tab_handles_2
    assert number_of_tab_handles_1 == 1
    assert number_of_tab_handles_2 == 2
