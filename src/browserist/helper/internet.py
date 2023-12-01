import multiprocessing
import ssl
from urllib import request
from urllib.error import URLError

from ..constant import timeout
from ..model.type.url import URL


def check_connection(url: URL, timeout: float = timeout.DEFAULT) -> bool:
    """Check if there is an internet connection by pinging a server."""

    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        request.urlopen(url, timeout=timeout)
        return True
    except (URLError, Exception):
        return False


def has_connection(timeout: float = timeout.DEFAULT) -> bool:
    """Check if there is an internet connection by pinging public Google DNS servers.

    Reference: https://developers.google.com/speed/public-dns/docs/using"""

    google_dns_server_1_url = URL("https://8.8.8.8")
    google_dns_server_2_url = URL("https://8.8.4.4")
    urls = [google_dns_server_1_url, google_dns_server_2_url]

    with multiprocessing.Pool(len(urls)) as pool:
        return any(pool.starmap(check_connection, [(url, timeout) for url in urls]))
