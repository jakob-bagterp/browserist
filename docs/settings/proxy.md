---
title: How to Configure a Proxy
description: Learn how to set a proxy server to bypass network restrictions and maintain anonymity while web scraping. With Browserist as extension to Selenium, it's easy to configure with few lines of code.
tags:
    - Tutorial
    - Settings
    - Proxy
---

# What Is a Proxy and Why Using It?
A proxy server acts as an intermediary between your browser and the internet. Here are five common use cases for using a proxy server:

1. **Enhanced security and privacy**: By routing your internet traffic through a proxy server, you can hide your IP address and protect your personal information from potential threats.

2. **Accessing geo-restricted content**: Proxies can help you bypass geo-restrictions and access content that is not available in your region by masking your IP address with one from a different location.

3. **Improved performance**: Some proxy servers cache frequently accessed web pages, which can speed up your browsing experience by reducing the load time for those pages.

4. **Bypassing network restrictions**: In environments with strict network restrictions, such as schools or workplaces, proxies can help you access blocked websites and services.

5. **Anonymity**: When performing web scraping, using a proxy server can help you avoid IP bans and maintain anonymity, allowing you to gather data more effectively.

By understanding these use cases, you can determine whether using a proxy server is beneficial for your specific needs and context.

## Types of Proxies
There are two types of proxy servers:

| 1. Public proxy                                                                            | 2. Private proxy                                   |
| :----------------------------------------------------------------------------------------: | :------------------------------------------------: |
| These are accessible from the internet and are usually free to use without authentication. | These are usually paid and require authentication. |

!!! tip
    When using [public proxies](#public-proxy), be aware that they may be unreliable and slow. It's recommended to use a [private proxy](#private-proxy) for more consistent performance. Also, keep in mind that public proxies may not be available in all regions, they may have usage limitations, they may be blocked by your internet service provider, or they may be blocked by the website you're trying to access.

## How to Set a Proxy
Learn how to set a proxy for the needs and context of your automation workflow with Browserist.

### Public Proxy
Public proxies are accessible from the internet and are usually free to use without authentication.

#### Basic Usage
Example:

```python linenums="1" hl_lines="3"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(proxy="http://127.0.0.1:8080")

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

#### With `ProxySettings` Configuration Class
If you want to use the `ProxySettings` configuration class instead, here's how:

```python linenums="1" hl_lines="3-6"
from browserist import Browser, BrowserSettings, ProxySettings, ProxyProtocol

proxy_settings = ProxySettings(
    ip="127.0.0.1",
    port=8080,
    protocol=ProxyProtocol.HTTP)

settings = BrowserSettings(proxy=proxy_settings)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

### Private Proxy
Ensure that you have the necessary credentials to access a private proxy server before using it.

#### Basic Usage
Change the `username` and `password` values of the proxy string to match your credentials:

```python linenums="1" hl_lines="3"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(proxy="http://username:password@127.0.0.1:8080")

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

#### With `ProxySettings` Configuration Class
If you want to use the `ProxySettings` configuration class instead, here's how:

```python linenums="1" hl_lines="3-8"
from browserist import Browser, BrowserSettings, ProxySettings, ProxyProtocol

proxy_settings = ProxySettings(
    ip="127.0.0.1",
    port=8080,
    protocol=ProxyProtocol.HTTP
    username="username",
    password="password")

settings = BrowserSettings(proxy=proxy_settings)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

## Supported Browsers

!!! note
    Only a few browsers support using a proxy server, for instance Chrome, Edge, and Firefox.

Browsers that support using a proxy server for browser automation:

<div id="proxy-supported-browsers-table"></div>

| Chrome           | Edge             | Firefox           | Safari                          | Internet Explorer               |
| :--------------: | :--------------: | :---------------: | :-----------------------------: | :-----------------------------: |
| :material-check: | :material-check: | :material-check:  | :material-minus-circle-outline: | :material-minus-circle-outline: |


When configuring the proxy, use either a string with the IP address and port number, or the `ProxySettings` class:

<div id="proxy-settings-browser-support-table"></div>

| Settings Type                                       | Chrome           | Edge             | Firefox                         |
| :-------------------------------------------------- | :--------------: | :--------------: | :-----------------------------: |
| `str` with IP address, e.g. `http://127.0.0.1:8080` | :material-check: | :material-check: | :material-minus-circle-outline: |
| `ProxySettings`                                     | :material-check: | :material-check: | :material-check:                |
