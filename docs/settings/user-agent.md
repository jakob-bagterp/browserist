---
title: How to Configure User Agent
description: Learn how to set and customize the user agent string in Browserist. Includes code examples, tips, and tricks for web automation and scraping.
tags:
    - Tutorial
    - Settings
---

# What Is a User Agent?
Browsers identify themselves to websites with a `User-Agent` string in the request header. The user agent string contains information about:

* Browser type
* Browser version
* Operating system and platform

Websites use this information to provide the best possible user experience, or sometimes to block certain features or identify automated bots so that they can be excluded from analytics.

User agents come in many forms and can look like this:

```shell title=""
Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0
```

Learn more about [user agents and what they can do](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent).

## How to Set User Agent
!!! note
    Few browsers allow you to set the `User-Agent` on the fly, but most allow you to set it at the start of a session. [See below](#supported-browsers) for details.

### For a Session
How to set the user agent in the beginning of a session:

```python linenums="1" hl_lines="3 7-8"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(user_agent="MyUserAgent")

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    user_agent = browser.user_agent.get()
    print(user_agent)
```

How it appears in the terminal:

```shell title=""
MyUserAgent
```

### On the Fly
#### Basic Usage:

```python linenums="1" hl_lines="4"
from browserist import Browser

with Browser() as browser:
    browser.user_agent.set("MyUserAgent")
    browser.open.url("https://example.com")
    user_agent = browser.user_agent.get()
    print(user_agent)
```

How it appears in the terminal:

```shell title=""
MyUserAgent
```

#### Append to Existing User Agent:
If you want to identify your sessions, for instance to exclude bot traffic from your analytics, you can append the existing user agent with a custom value. Imagine that a browser's default user agent is:

```shell title=""
Mozilla/5.0
```

Let's add a custom value to it:

```python linenums="1" hl_lines="4-6"
from browserist import Browser

with Browser() as browser:
    user_agent = browser.user_agent.get()
    user_agent += " MyUserAgent"
    browser.user_agent.set(user_agent)
    browser.open.url("https://example.com")
    new_user_agent = browser.user_agent.get()
    print(new_user_agent)
```

How the user agent now appears in the terminal:

```shell title=""
Mozilla/5.0 MyUserAgent
```

### Supported Browsers
Most browsers support setting the `User-Agent` at the start of a session, but only a few allow you to set it on the fly:

<div id="user-agent-supported-browsers-table"></div>

| Case          | Chrome           | Edge             | Firefox                         | Safari                          | Internet Explorer               |
| :------------ | :--------------: | :--------------: | :-----------------------------: | :-----------------------------: | :-----------------------------: |
| For a session | :material-check: | :material-check: | :material-check:                | :material-check:                | :material-minus-circle-outline: |
| On the fly    | :material-check: | :material-check: | :material-minus-circle-outline: | :material-minus-circle-outline: | :material-minus-circle-outline: |

## How to Randomize User Agent
As example for advanced usage, you can randomize the user agent per session or on the fly.

### Per Session
Example:

```python linenums="1" hl_lines="10-11"
import random
from browserist import Browser, BrowserSettings

USER_AGENTS = [
    "MyUserAgent1",
    "MyUserAgent2",
    "MyUserAgent3",
]

user_agent = random.choice(USER_AGENTS)
settings = BrowserSettings(user_agent=user_agent)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

### On the Fly
Example:

```python linenums="1" hl_lines="11-12"
import random
from browserist import Browser

USER_AGENTS = [
    "MyUserAgent1",
    "MyUserAgent2",
    "MyUserAgent3",
]

with Browser() as browser:
    user_agent = random.choice(USER_AGENTS)
    browser.user_agent.set(user_agent)
    browser.open.url("https://example.com")
```
