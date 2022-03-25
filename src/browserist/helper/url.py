def ensure_trailing_slash(url: str) -> str:
    """When comparing URLs, e.g. "http://example.com/" and "http://example.com", use this method to normalise the comparison."""

    if "?" in url:  # If the URL contains a parameter (e.g. https://example.com/search?page=1), ignore trailing slash.
        return url
    return url if url[-1] == "/" else f"{url}/"


def is_https(url: str) -> bool:
    return url.startswith("https:")


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
