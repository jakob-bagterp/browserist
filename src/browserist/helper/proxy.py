from ..model.browser.base.proxy import ProxySettings


def get_url_from_proxy_settings(proxy_settings: ProxySettings, add_protocol: bool = True, add_port: bool = True) -> str:
    """Returns a proxy server based on the settings.

    Args:
        proxy (ProxySettings): Proxy settings.

    Returns:
        Proxy URL. Examples: `http://127.0.0.1:8080` or `http://username:password@127.0.0.1:8080`. Or without port number: `http://127.0.0.1` or `http://username:password@127.0.0.1`. Or without port number and protocol: `127.0.0.1` or `username:password@127.0.0.1`.
    """

    username_and_password = (
        f"{proxy_settings.username}:{proxy_settings.password}@"
        if proxy_settings.username and proxy_settings.password
        else ""
    )
    port = f":{proxy_settings.port}" if add_port else ""
    protocol = f"{proxy_settings.type.value}://" if add_protocol else ""
    return f"{protocol}{username_and_password}{proxy_settings.ip}{port}"
