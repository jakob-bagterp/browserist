from _helper.type import validate_bypass
from _mock_data.url.test_set_2 import VALID_URL

from browserist.model.type.url import URL


def test_url_type_bypass_if_already_xpath() -> None:
    """Test that if an input already is a validated URL element, bypass and don't create a new object."""

    validate_bypass(URL, VALID_URL)
