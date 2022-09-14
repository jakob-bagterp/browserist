import re


def tool_is_input_valid(text: str, regex: str, ignore_case: bool = True) -> bool:
    match = re.fullmatch(regex, text, re.IGNORECASE) if ignore_case else re.fullmatch(regex, text)
    return bool(match)
