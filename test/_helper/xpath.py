from contextlib import nullcontext as does_not_raise
from dataclasses import dataclass
from typing import Any

import pytest

from browserist.exception.xpath import XPathSyntaxError


@dataclass(frozen=True)
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
