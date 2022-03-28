from ... import helper


def tool_is_url_valid(url: str) -> bool:
    return helper.url.is_valid(url)
