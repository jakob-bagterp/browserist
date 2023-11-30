from urllib import request
from urllib.error import URLError

from ..model.type.url import URL


def check_connection(url: URL, timeout: float = 1) -> bool:
    """Check if there is an internet connection by pinging a server."""

    try:
        request.urlopen(url, timeout=timeout)
        return True
    except (URLError, Exception):
        return False


def has_connection() -> bool:
    """Check if there is an internet connection by pinging public Google DNS servers.

    Reference: https://developers.google.com/speed/public-dns/docs/using"""

    google_dns_server_1_url = URL("https://8.8.8.8")
    google_dns_server_2_url = URL("https://8.8.4.4")

    # TODO: Refactor to async.

    return check_connection(google_dns_server_1_url) or check_connection(google_dns_server_2_url)
