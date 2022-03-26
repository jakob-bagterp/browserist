from contextlib import nullcontext as does_not_raise
from dataclasses import dataclass
from typing import Any

import pytest

from browserist import Browser
from browserist.exception.xpath import XPathSyntaxError
from browserist.model.type.callable import (BrowserMethodWith2ArgumentsCallable, BrowserMethodWith3ArgumentsCallable,
                                            BrowserMethodWith4ArgumentsCallable)

from . import internal_url


@dataclass(frozen=True, slots=True)
class XPathExpectation:
    xpath: str
    expactation: Any


# Should be compatible with general web pages so it can be used with wait methods without timing out:
VALID_XPATH = "/html/body"

INVALID_XPATH = "/invalid\\xpath"

XPATH_TESTS: list[XPathExpectation] = [
    XPathExpectation(VALID_XPATH, does_not_raise()),
    XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
]

# Compatible with Example.com so it can be used with wait methods without timing out:
VALID_XPATH_EXAMPLE_COM = "/html/body/div/p[2]/a"

XPATH_TESTS_EXAMPLE_COM: list[XPathExpectation] = [
    XPathExpectation(VALID_XPATH_EXAMPLE_COM, does_not_raise()),
    XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
]

# Compatible with W3Schools.com so it can be used with wait methods without timing out:
VALID_XPATH_W3SCHOOLS_COM_IMAGE = "//*[@id='bgcodeimg2']/div/img"

XPATH_TESTS_W3SCHOOLS_COM_IMAGE: list[XPathExpectation] = [
    XPathExpectation(VALID_XPATH_W3SCHOOLS_COM_IMAGE, does_not_raise()),
    XPathExpectation(INVALID_XPATH, pytest.raises(XPathSyntaxError)),
]


def exception_handling_for_methods_with_2_arguments(
    browser: Browser,
    method: BrowserMethodWith2ArgumentsCallable,
    url: str = internal_url.EXAMPLE_COM,
    tests: list[XPathExpectation] = XPATH_TESTS
) -> None:
    browser.open.url(url)
    for test in tests:
        with test.expactation:
            _ = method(browser.driver, test.xpath) is not None


def exception_handling_for_methods_with_3_arguments_or_more(
    browser: Browser,
    method: BrowserMethodWith3ArgumentsCallable | BrowserMethodWith4ArgumentsCallable,
    *args: Any,
    url: str = internal_url.EXAMPLE_COM,
    tests: list[XPathExpectation] = XPATH_TESTS_EXAMPLE_COM
) -> None:
    browser.open.url(url)
    for test in tests:
        with test.expactation:
            _ = method(browser.driver, test.xpath, *args) is not None
