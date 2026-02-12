from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _mock_data.url.test_set_2 import INVALID_URL, VALID_URL
from _mock_data.xpath.constant import VALID_XPATH

from browserist.constant import timeout
from browserist.exception.url import URLSyntaxError
from browserist.model.combo_settings.login_form import LoginForm2Steps


@pytest.mark.parametrize(
    "url, expectation", [(VALID_URL, does_not_raise()), (INVALID_URL, pytest.raises(URLSyntaxError))]
)
def test_url_exception_handling_of_login_form_2_steps(url: str, expectation: Any) -> None:
    with expectation:
        _ = (
            LoginForm2Steps(
                username_input_xpath=VALID_XPATH,
                username_submit_button_xpath=VALID_XPATH,
                password_input_xpath=VALID_XPATH,
                password_submit_button_xpath=VALID_XPATH,
                url=url,
                post_login_wait_seconds=timeout.VERY_SHORT,
                post_login_url_contains=VALID_URL,
                post_login_element_xpath=VALID_XPATH,
            )
            is not None
        )
