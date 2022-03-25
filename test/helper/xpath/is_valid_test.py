from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from browserist import helper
from browserist.exception.xpath import XPathSyntaxError


@pytest.mark.parametrize("xpath, expectation", [
    ("//*[@id='react-root']/section", does_not_raise()),
    ("//*[[@id='react-root']/section", pytest.raises(XPathSyntaxError)),
    ("//*[@id='react-root']\\section", pytest.raises(XPathSyntaxError)),
])
def test_helper_window_handle_is_valid_id(xpath: str, expectation: Any) -> None:
    with expectation:
        _ = helper.xpath.is_valid(xpath) is not None
