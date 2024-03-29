import pytest
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser


@pytest.mark.parametrize("url, xpath, expected_texts", [
    (internal_url.EXAMPLE_COM, "/html/body/div/p[2]/a", ["More information..."]),
    (internal_url.EXAMPLE_COM, "/html/body/div/p",
     ["This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.", "More information..."]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[9]/div/a[1]", ["Try Frontend Editor (HTML/CSS/JS)"]),
    (internal_url.W3SCHOOLS_COM, "//*[@id='main']/div[2]/div/div[1]/a",
     ["Learn HTML", "Video Tutorial\nNEW", "HTML Reference"]),
])
def test_get_texts(url: str, xpath: str, expected_texts: str, browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(url)
    assert browser.get.texts(xpath) == expected_texts
