from browserist import Browser

browser = Browser()

print("window_size", browser.window.get.size())
print("window_position", browser.window.get.position())
browser.window.set.position(0, 0)
print("window_position", browser.window.get.position())

browser.open.url_if_not_current("https://www.dr.dk/")
browser.window.set.size(300, 300)
print("window_size", browser.window.get.size())
browser.window.minimize()
browser.window.maximize()
browser.window.fullscreen()

browser.window.open.new_tab("https://github.com/jakob-bagterp/")
print("current_handle", browser.window.handle.current())
print(browser.get.url.current())
browser.window.open.new_tab()
browser.window.close()
browser.window.open.new_window()
window_handle = browser.window.handle.current()
print("", window_handle)
browser.window.switch_to_original_window()
browser.window.switch_to(window_handle)
browser.window.close()
browser.quit()
