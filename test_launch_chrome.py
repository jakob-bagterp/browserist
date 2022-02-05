import time
from src.browserist import Browser

browser = Browser()

browser.open.url("https://www.dr.dk/")

browser.refresh()

#browser.get("https://github.com/jakob-bagterp/")
browser.open.url("https://github.com/jakob-bagterp/")

browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")

time.sleep(5)

#browser.get("https://www.google.dk/")

browser.open.url_if_not_current("https://www.google.dk")

browser.back()
browser.forward()

browser.quit()
