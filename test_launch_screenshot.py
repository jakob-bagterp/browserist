from src.browserist import Browser

browser = Browser()

browser.open.url("https://github.com/jakob-bagterp/")
browser.get.screenshot()
browser.scroll.to_end_of_page()
browser.get.screenshot()
browser.scroll.to_position(100, 100)
browser.get.screenshot()
browser.scroll.to_top_of_page()
browser.get.screenshot()

browser.quit()
