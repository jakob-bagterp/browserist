from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url.test_set_2 import VALID_URL
from _mock_data.xpath.constant import INVALID_XPATH, VALID_XPATH

from browserist.constant import timeout
from browserist.exception.xpath import XPathSyntaxError
from browserist.model.combo_settings.login_form import LoginForm2Steps


@pytest.mark.parametrize(
    "xpath1, xpath2, xpath3, xpath4, xpath5, expectation",
    [
        (VALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, does_not_raise()),
        (INVALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
        (VALID_XPATH, INVALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
        (VALID_XPATH, VALID_XPATH, INVALID_XPATH, VALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
        (VALID_XPATH, VALID_XPATH, VALID_XPATH, INVALID_XPATH, VALID_XPATH, pytest.raises(XPathSyntaxError)),
        (VALID_XPATH, VALID_XPATH, VALID_XPATH, VALID_XPATH, INVALID_XPATH, pytest.raises(XPathSyntaxError)),
    ],
)
def test_xpath_exception_handling_of_login_form_2_steps(
    xpath1: str, xpath2: str, xpath3: str, xpath4: str, xpath5: str, expectation: Any
) -> None:
    with expectation:
        _ = (
            LoginForm2Steps(
                username_input_xpath=xpath1,
                username_submit_button_xpath=xpath2,
                password_input_xpath=xpath3,
                password_submit_button_xpath=xpath4,
                url=VALID_URL,
                post_login_wait_seconds=timeout.VERY_SHORT,
                post_login_url_contains=VALID_URL,
                post_login_element_xpath=xpath5,
            )
            is not None
        )
