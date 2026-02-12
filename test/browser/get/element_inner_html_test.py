import _helper
from _helper.timeout import reset_to_not_timed_out
from _mock_data.url import internal_url

from browserist import Browser

EXPECTED_INNER_HTML = """
<div class="hero__text-box">
    <h1>Welcome</h1>
    <p>Discover the best products for your needs.</p>
    <a href="#" class="cta-button">Get Started</a>
</div>
"""


def test_get_element_inner_html(browser_default_headless: Browser) -> None:
    browser = reset_to_not_timed_out(browser_default_headless)
    browser.open.url(internal_url.MINI_SITE_HOMEPAGE)
    inner_html = browser.get.html.element_inner(
        "//section[@class='hero hero__background-image__office-ideas-on-board']"
    )
    inner_html_stripped = _helper.html.strip_whitespace(inner_html)
    expected_inner_html_stripped = _helper.html.strip_whitespace(EXPECTED_INNER_HTML)
    assert inner_html_stripped == expected_inner_html_stripped
