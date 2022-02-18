import re
from ... import constant

_url_pattern = re.compile(constant.regex.VALID_URL, re.IGNORECASE)

def tool_is_url_valid(url: str) -> bool:
    return bool(_url_pattern.match(url))
