import time
from src.browserist import Browser

browser = Browser()

browser.open.url("https://www.dr.dk/")

browser.refresh()

#browser.get("https://github.com/jakob-bagterp/")
browser.open.url("https://github.com/jakob-bagterp/")
xpath = "/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/a/img"
browser.wait.for_element(xpath)
print(browser.check_if.is_element_clickable(xpath))
print(browser.check_if.is_element_disabled(xpath))
print(browser.check_if.is_element_enabled(xpath))

browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")
browser.open.url_if_not_current("https://www.dr.dk/")

browser.open.url_in_new_tab("https://github.com/jakob-bagterp/")
print(browser.get.current_url())

time.sleep(5)

#browser.get("https://www.google.dk/")

browser.open.url_if_not_current("https://www.google.dk")

browser.back()
browser.forward()

browser.quit()
