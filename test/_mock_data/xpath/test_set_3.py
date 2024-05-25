from contextlib import nullcontext as does_not_raise

import pytest
from _mock_data.url import internal_url
from _mock_data.xpath.model_3 import XPathExpectation, XPathTestSet

from browserist.exception.xpath import XPathSyntaxError

# Should be compatible with general web pages so it can be used with wait methods without timing out:
VALID_XPATH = "/html/body"

INVALID_XPATH = "/invalid\\xpath"

XPATH_TEST_SET_MINI_SITE_HOMEPAGE_DEFAULT = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation(VALID_XPATH, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

VALID_XPATH_MINI_SITE_HOMEPAGE_LINK = "/html/body/section[2]/div[1]/a"

XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation(VALID_XPATH_MINI_SITE_HOMEPAGE_LINK, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

VALID_XPATH_MINI_SITE_FEATURE_1_IMAGE = "//*[@id='main']/img[1]"

XPATH_TEST_SET_MINI_SITE_FEATURE_1_IMAGE = XPathTestSet(
    url=internal_url.MINI_SITE_FEATURE_1,
    tests=[
        XPathExpectation(VALID_XPATH_MINI_SITE_FEATURE_1_IMAGE, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

VALID_XPATH_MINI_SITE_HOMEPAGE_HEADLINE = "/html/body/section[1]/div/h1"

XPATH_TEST_SET_W3SCHOOLS_COM_HEADLINE = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation(VALID_XPATH_MINI_SITE_HOMEPAGE_HEADLINE, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

VALID_XPATH_W3SCHOOLS_COM_IFRAME = "//*[@id='howto_iframe']"

XPATH_TEST_SET_W3SCHOOLS_COM_IFRAME = XPathTestSet(
    url=internal_url.W3SCHOOLS_COM,
    tests=[
        XPathExpectation(VALID_XPATH_W3SCHOOLS_COM_IFRAME, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

VALID_XPATH_W3SCHOOLS_COM_INPUT = "//*[@id='search2']"

XPATH_TEST_SET_W3SCHOOLS_COM_INPUT = XPathTestSet(
    url=internal_url.W3SCHOOLS_COM,
    tests=[
        XPathExpectation(VALID_XPATH_W3SCHOOLS_COM_INPUT, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)
