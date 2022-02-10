from src.browserist import Browser, CookieBannerSettings, SearchSettings

browser = Browser()

url = "https://www.google.dk/"

accept_cookies_xpath = "//*[@id='L2AGLb']"
cookie_banner_settings = CookieBannerSettings(button_xpath = accept_cookies_xpath, url = url)
browser.combo.cookie_banner(cookie_banner_settings)

input_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
button_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]"
search_settings = SearchSettings(input_xpath, button_xpath, url = url)
browser.combo.search("browser automation", search_settings)
browser.wait.until_url_changes(url)

browser.quit()
