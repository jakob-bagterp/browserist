import re
from ... import constant

def tool_is_url_valid(url: str) -> bool:
    return bool(re.match(constant.regex.VALID_URL, url, re.IGNORECASE))
