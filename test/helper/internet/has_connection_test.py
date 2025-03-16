from browserist import helper


def test_helper_internet_has_connection() -> None:
    assert helper.internet.has_connection() is True
