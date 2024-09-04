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


HTTP_OR_HTTPS_REGEX_PATTERN = "https?:"


def compile_comparison_to_regex_pattern(url: str | URL, ignore_trailing_slash: bool, ignore_parameters: bool, ignore_https: bool) -> re.Pattern[str]:
    """Compile a URL to a regular expression pattern with optionals for comparison.

    Args:
        url (str | URL): URL to compile to a regular expression pattern.
        ignore_trailing_slash (bool): Ignore whether the URL is `"https://example.com"` or `"https://example.com/"`.
        ignore_parameters (bool): Ignore parameters in the URL, e.g. `?page=1` in `"https://example.com/articles?page=1"`.
        ignore_https (bool): Ignore whether the URL is `"http://example.com"` or `"https://example.com"`.

    Returns:
        re.Pattern[str]: Intended to be used for comparison with other URLs, e.g. `url_pattern.fullmatch(url_to_compare)`
    """

    def handle_ignore_trailing_slash(url: str, ignore_trailing_slash: bool) -> str:
        """Makes trailing slash optional, e.g. `"some/page/?"`, if needed. Note that the input URL should be without parameters."""

        if ignore_trailing_slash:
            if url.endswith("/"):
                url += "?"
            else:
                url += "/?"
        return url

    def handle_ignore_https(url: str, ignore_https: bool) -> str:
        """Makes HTTPS optional, e.g. `"https?://example.com"`. Note that the input URL should be without parameters."""

        if ignore_https:
            if url.startswith(HTTP):
                url = url.replace(HTTP, HTTP_OR_HTTPS_REGEX_PATTERN, 1)
            elif url.startswith(HTTPS):
                url = url.replace(HTTPS, HTTP_OR_HTTPS_REGEX_PATTERN, 1)
        return url

    def escape_question_mark(parameters: str) -> str:
        return parameters.replace("?", r"\?")

    url_has_parameters = has_parameters(url)
    url, parameters = split_url_and_parameters(url)
    url = handle_ignore_trailing_slash(url, ignore_trailing_slash)
    url = handle_ignore_https(url, ignore_https)
    if url_has_parameters and not ignore_parameters:
        parameters = escape_question_mark(parameters)
        return re.compile(f"^{url}{parameters}$", re.IGNORECASE)
    else:
        return re.compile(f"^{url}", re.IGNORECASE)
