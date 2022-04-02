from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from _helper.xpath.test_set_2 import VALID_XPATH
from _mock_data.url.test_set_1 import INVALID_URL, VALID_URL

from browserist.constant import timeout
from browserist.exception.url import URLSyntaxError
from browserist.model.combo_settings.cookie_banner import CookieBannerSettings


@pytest.mark.parametrize("url, expectation", [
    (VALID_URL, does_not_raise()),
    (INVALID_URL, pytest.raises(URLSyntaxError)),
])
def test_url_exception_handling_of_cookie_bannger_settings(url: str, expectation: Any) -> None:
    with expectation:
        _ = CookieBannerSettings(
            button_xpath=VALID_XPATH,
            url=url,
            has_loaded_xpath=VALID_XPATH,
            has_disappeared_wait_seconds=timeout.VERY_SHORT
        ) is not None
