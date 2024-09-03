import re
from urllib.parse import urlparse

from ..model.type.url import URL

HTTP = "http:"
HTTPS = "https:"


def ensure_trailing_slash(url: str | URL) -> str:
    """When comparing URLs, e.g. "https://example.com" and "https://example.com/", use this method to normalise the comparison."""

    if "?" in url:  # If the URL contains a parameter (e.g. "https://example.com/search?page=1"), ignore trailing slash.
        return url
    return url if url[-1] == "/" else f"{url}/"


def is_https(url: str | URL) -> bool:
    return url.startswith(HTTPS)


def is_valid(url: str | URL) -> bool:
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
        url1 = url1.replace(HTTP, HTTPS)
    elif not is_https(url2):
        url2 = url2.replace(HTTP, HTTPS)
    return url1, url2


def remove_parameters(url: str | URL) -> str:
    return url if "?" not in url else url.split("?")[0]


def has_parameters(url: str | URL) -> bool:
    """If a URL contains one or more parameters, e.g. `https://example.com/search?page=1`."""

    return True if "?" in url else False


def split_url_and_parameters(url: str | URL) -> tuple[str, str]:
    """Split URL and parameters, e.g. `https://example.com/search?page=1` into `https://example.com/search` and `?page=1`.

    Args:
        url (str): URL with out without parameters.

    Returns:
        tuple[str, str]: Example: `url, parameters = split_url_and_parameters(url)`
    """

    if not has_parameters(url):
        return url, ""
    url, parameters = url.split("?", 1)
    return url, f"?{parameters}"


def get_domain_from_url(url: str | URL) -> str:
    return (urlparse(url).netloc)


HTTP_OR_HTTPS_REGEX = "https?:"


def compile_comparison_to_regex_pattern(url: str | URL, ignore_trailing_slash: bool, ignore_parameters: bool, ignore_https: bool) -> re.Pattern[str]:
    url_has_parameters = has_parameters(url)

    if ignore_parameters:
        url = remove_parameters(url)
    elif url_has_parameters:
        url = url.replace("?", r"\?")  # Ensure that ? is escaped and treated as a special character in the URL.

    if ignore_trailing_slash:  # Makes trailing slash optional, e.g.: "some/page/?"
        if url.endswith("/"):
            url += "?"
        elif not url_has_parameters:
            url += "/?"
        elif url_has_parameters:
            url = url.replace(r"/\?", r"/?\?").replace(r"\?", r"/?\?")

    if ignore_https:
        if url.startswith(HTTP):
            url = url.replace(HTTP, HTTP_OR_HTTPS_REGEX, 1)
        elif url.startswith(HTTPS):
            url = url.replace(HTTPS, HTTP_OR_HTTPS_REGEX, 1)

    if url_has_parameters:
        return re.compile(f"^{url}$", re.IGNORECASE)
    else:
        return re.compile(f"^{url}", re.IGNORECASE)
