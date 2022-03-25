from browserist import Browser

from .._helper import internal_url

with Browser() as browser:
    browser.open.url(internal_url.W3SCHOOLS_COM)

    element_1_xpath = "//*[@id='main']/div[1]/div/h1"
    print("is_element_displayed", element_1_xpath, browser.check_if.is_element_displayed(element_1_xpath))
    browser.scroll.into_view(element_1_xpath)

    element_2_xpath = "//*[@id='main']/footer"
    print("is_element_displayed", element_2_xpath, browser.check_if.is_element_displayed(element_2_xpath))
    browser.scroll.into_view(element_2_xpath)

    element_3_xpath = "//*[@id='google_translate_element']"
    print("is_element_displayed", element_3_xpath, browser.check_if.is_element_displayed(element_3_xpath))
    browser.scroll.into_view(element_3_xpath)
