from _mock_data.url.test_set_2 import VALID_URL

from browserist.model.type.url import URL


def test_url_type_representation() -> None:
    """Test that the XPath tiny type represents itself as a an URL string."""

    url_input = expected_url_output = VALID_URL
    url_type = URL(url_input)
    assert expected_url_output == url_type
    assert expected_url_output == url_type.value
