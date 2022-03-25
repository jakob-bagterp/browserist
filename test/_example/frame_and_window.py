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

browser.open.new_tab("https://github.com/jakob-bagterp/")
print("current_handle", browser.window.get.current_handle())
print(browser.get.url.current())
browser.open.new_tab()
browser.window.close()
browser.open.new_window()
window_handle = browser.window.get.current_handle()
print("", window_handle)
browser.switch_to.original_window()
browser.switch_to.window(window_handle)
browser.window.close()
browser.quit()
