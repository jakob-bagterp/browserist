import re

def tool_is_input_valid(text: str, regex: str, ignore_case: bool = True) -> bool:
    if ignore_case:
        match = re.match(regex, text, re.IGNORECASE)
    else:
        match = re.match(regex, text)
    return bool(match)
