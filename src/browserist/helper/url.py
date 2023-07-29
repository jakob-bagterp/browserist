from urllib.parse import urlparse

from ..model.type.url import URL


def ensure_trailing_slash(url: str) -> str:
    """When comparing URLs, e.g. "https://example.com" and "https://example.com/", use this method to normalise the comparison."""

    if "?" in url:  # If the URL contains a parameter (e.g. "https://example.com/search?page=1"), ignore trailing slash.
        return url
    return url if url[-1] == "/" else f"{url}/"


def is_https(url: str) -> bool:
    return url.startswith("https:")


def is_valid(url: str) -> bool:
    if url.startswith("file://"):  # Accept files from local machine as valid URL and as an exception.
        return True
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def mediate_conversion_to_tiny_type_or_none(value: str | None) -> URL | None:
    """Mediate conversion of string to URL tiny type or keep None type."""

    return None if value is None else URL(value)


def mediate_https(url1: str, url2: str) -> tuple[str, str]:
    """If a URL is HTTPS, the other URL should also be HTTPS."""

    if (is_https(url1) and is_https(url2)) or (not is_https(url1) and not is_https(url2)):
        return url1, url2
    elif not is_https(url1):
        url1 = url1.replace("http:", "https:")
    elif not is_https(url2):
        url2 = url2.replace("http:", "https:")
    return url1, url2


def remove_parameters(url: str) -> str:
    return url if "?" not in url else url.split("?")[0]


def get_domain_from_url(url: str) -> str:
    return (urlparse(url).netloc)
