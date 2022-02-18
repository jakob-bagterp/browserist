import re

def tool_is_input_valid(text: str, regex: str, ignore_case: bool = True) -> bool:
    if ignore_case:
        match = re.fullmatch(regex, text, re.IGNORECASE)
    else:
        match = re.fullmatch(regex, text)
    return bool(match)
