def ensure_trailing_slash(url: str) -> str:
    if "?" in url:  # If the URL contains a parameter (e.g. https://example.com/search?page=1), ignore trailing slash.
        return url
    return url if url[-1] == "/" else f"{url}/"
