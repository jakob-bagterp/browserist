import re


def is_value_valid(value: str, regex: str) -> bool:
    return True if re.match(regex, value) else False
