from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.xpath.constant import INVALID_XPATH, VALID_XPATH

from browserist.exception.xpath import XPathSyntaxError
from browserist.model.type.xpath import XPath


@pytest.mark.parametrize(
    "xpath, expectation, is_valid_expectation",
    [(VALID_XPATH, does_not_raise(), True), (INVALID_XPATH, pytest.raises(XPathSyntaxError), False)],
)
def test_xpath_type_is_valid(xpath: str, expectation: Any, is_valid_expectation: bool) -> None:
    with expectation:
        xpath = XPath(xpath)
        assert xpath.is_valid() == is_valid_expectation
