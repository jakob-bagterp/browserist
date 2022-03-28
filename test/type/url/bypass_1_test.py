from _helper.url.test_set_1 import VALID_URL

from browserist.model.type.url import URL


def test_url_type_bypass_if_already_xpath() -> None:
    """Test that if an input already is a validated URL element, bypass and don't create a new object."""

    url_type = URL(VALID_URL)
    assert url_type is URL(url_type)
    assert URL(VALID_URL) is not URL(VALID_URL)
