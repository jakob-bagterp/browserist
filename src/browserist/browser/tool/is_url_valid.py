from urllib.parse import urlparse


def tool_is_url_valid(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except (ValueError, Exception):
        return False
