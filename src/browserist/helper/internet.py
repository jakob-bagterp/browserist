import multiprocessing
import ssl

import requests
from requests import Session

from ..constant import timeout
from ..model.type.url import URL


def check_connection(url: URL, requests_session: Session, timeout: float = timeout.DEFAULT) -> bool:
    """Check if there is an internet connection by pinging a server."""

    try:
        ssl._create_default_https_context = ssl._create_unverified_context  # type: ignore
        _ = requests_session.get(url, timeout=timeout)
        return True
    except (ConnectionError, Exception):
        return False


def has_connection(timeout: float = timeout.DEFAULT) -> bool:
    """Check if there is an internet connection by pinging public Cloudflare and Google DNS servers. References:

    https://developers.google.com/speed/public-dns/docs/using
    https://www.cloudflare.com/en-gb/learning/dns/what-is-1.1.1.1/"""

    cloudflare_dns_server_1_url = URL("https://1.1.1.1")
    cloudflare_dns_server_2_url = URL("https://1.0.0.1")
    google_dns_server_1_url = URL("https://8.8.8.8")
    google_dns_server_2_url = URL("https://8.8.4.4")
    urls = [cloudflare_dns_server_1_url, cloudflare_dns_server_2_url, google_dns_server_1_url, google_dns_server_2_url]
    with requests.Session() as requests_session:
        check_connection_args = [(url, requests_session, timeout) for url in urls]
        number_of_processes = len(urls)
        with multiprocessing.Pool(processes=number_of_processes) as pool:
            list_of_results = pool.starmap(check_connection, check_connection_args)
            return any(list_of_results)
