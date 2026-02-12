from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.xpath.constant import INVALID_XPATH, VALID_XPATH

from browserist.exception.xpath import XPathSyntaxError
from browserist.model.type.xpath import XPath


@pytest.mark.parametrize(
    "xpath, expectation",
    [
        (VALID_XPATH, does_not_raise()),
        (INVALID_XPATH, pytest.raises(XPathSyntaxError)),
        ("//*[@id='react-root']/section", does_not_raise()),
        ("//*[[@id='react-root']/section", pytest.raises(XPathSyntaxError)),
        ("//*[@id='react-root']\\section", pytest.raises(XPathSyntaxError)),
    ],
)
def test_xpath_type_exception_handling(xpath: str, expectation: Any) -> None:
    with expectation:
        _ = XPath(xpath) is not None
