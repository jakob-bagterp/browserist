from ..model.browser.base.proxy import ProxySettings


def get_url_from_proxy_settings(proxy_settings: ProxySettings) -> str:
    """Returns a proxy server based on the settings.

    Args:
        proxy (ProxySettings): Proxy settings.

    Returns:
        Proxy: Proxy URL. Examples: `http://127.0.0.1:8080` or `http://username:password@127.0.0.1:8080`.
    """

    username_and_password = f"{proxy_settings.username}:{proxy_settings.password}@" if proxy_settings.username and proxy_settings.password else ""
    return f"{proxy_settings.type.value}://{username_and_password}{proxy_settings.ip}:{proxy_settings.port}"
