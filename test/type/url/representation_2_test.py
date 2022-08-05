from _helper.type import validate_representation
from _mock_data.url.test_set_2 import VALID_URL

from browserist.model.type.url import URL


def test_url_type_representation() -> None:
    """Test that the XPath tiny type represents itself as a an URL string."""

    validate_representation(URL, VALID_URL)
