from contextlib import nullcontext as does_not_raise

import pytest
from _mock_data import does_not_exist
from _mock_data.url import internal_url
from _mock_data.xpath.constant import INVALID_XPATH, VALID_XPATH
from _mock_data.xpath.model_3 import XPathExpectation, XPathTestSet

from browserist.exception.xpath import XPathSyntaxError

XPATH_TEST_SET_MINI_SITE_HOMEPAGE_DEFAULT = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation(VALID_XPATH, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

XPATH_TEST_SET_MINI_SITE_HOMEPAGE_LINK = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation("/html/body/section[2]/div[1]/a", does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

XPATH_TEST_SET_MINI_SITE_HOMEPAGE_DOES_NOT_EXIST = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation(does_not_exist.XPATH, does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

XPATH_TEST_SET_MINI_SITE_FEATURE_1_IMAGE = XPathTestSet(
    url=internal_url.MINI_SITE_FEATURE_1,
    tests=[
        XPathExpectation("//*[@id='main']/img[1]", does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

XPATH_TEST_SET_MINI_SITE_HOMEPAGE_HEADLINE = XPathTestSet(
    url=internal_url.MINI_SITE_HOMEPAGE,
    tests=[
        XPathExpectation("/html/body/section[1]/div/h1", does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

XPATH_TEST_SET_COOKIE_BANNER_IFRAME = XPathTestSet(
    url=internal_url.COOKIE_BANNER_WITH_IFRAME,
    tests=[
        XPathExpectation("//iframe[@id='cookie-banner-iframe']", does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)

XPATH_TEST_SET_W3SCHOOLS_COM_INPUT = XPathTestSet(
    url=internal_url.MINI_SITE_CONTACT,
    tests=[
        XPathExpectation("//input[@id='subject']", does_not_raise()),
        XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ]
)
