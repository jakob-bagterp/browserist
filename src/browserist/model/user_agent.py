from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class UserAgentSettings:
    """Settings class to override the default or current `User-Agent` in the request header.

    Args:
        user_agent (str | None, optional): The user agent to set as `User-Agent` in the request header. If `None`, the default or current user agent is used.
        platform (str | None, optional): The platform to set as `Platform` in the request header. If `None`, the default or current platform is used.
    """

    user_agent: str | None = None
    platform: str | None = None
