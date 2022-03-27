from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper import internal_url
from _helper.xpath.test_set import INVALID_XPATH, VALID_XPATH

from browserist.constant import timeout
from browserist.exception.xpath import XPathSyntaxError
from browserist.model.combo_settings.login_form import LoginForm1Step


@pytest.mark.parametrize("xpath1, xpath2, xpath3, xpath4, expectation", [
    (VALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, does_not_raise()),
    (INVALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, INVALID_XPATH, VALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, VALID_XPATH, INVALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
    (VALID_XPATH, VALID_XPATH, VALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
])
def test_xpath_exception_handling_of_login_form_1_step(xpath1: str, xpath2: str, xpath3: str, xpath4: str, expectation: Any) -> None:
    with expectation:
        _ = LoginForm1Step(
            username_input_xpath=xpath1,
            password_input_xpath=xpath2,
            submit_button_xpath=xpath3,
            url=internal_url.EXAMPLE_COM,
            post_login_wait_seconds=timeout.VERY_SHORT,
            post_login_url=internal_url.EXAMPLE_COM,
            post_login_element_xpath=xpath4
        ) is not None
