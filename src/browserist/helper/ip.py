import re

IPV4_REGEX_PATTERN = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


def ipv4_is_valid(ip: str) -> bool:
    """Check if given string is a valid IPv4 address."""

    return IPV4_REGEX_PATTERN.fullmatch(ip) is not None and \
        all(0 <= int(num) <= 255 for num in ip.split(".") if num.isdigit())
