---
title: How to Configure Timeout Strategy
description: Should the browser stop or continue when a function times out or if something breaks? Learn how to set the best timeout strategy for the needs and context of your automation workflow.
tags:
    - Tutorial
    - Settings
    - Performance
---

# What Is a Timeout Strategy?
How long should the browser wait and keep retrying to interact with an element: 5, 10, or 20 seconds? And what happens when a function times out: Should the browser stop or continue its operation?

Learn how to set the best timeout strategy for the needs and context of your automation workflow.

## Settings and Strategy
`TimeoutSettings` defines the `TimeoutStrategy` together with a general timeout in seconds. For example:

```python linenums="1" hl_lines="3-5"
from browserist import TimeoutSettings, TimeoutStrategy

timeout_settings = TimeoutSettings(
    strategy=TimeoutStrategy.CONTINUE,
    seconds=10)
```

!!! tip
    The general timeout can often be shortened or lengthened by the function-specific timeout. It's recommended to keep the default of 5 seconds or to set the general timeout to a value that's sufficient for most functions – most methods run faster anyway – and then override it for specific functions.

### Options for `TimeoutSettings`

| Parameter  | Description                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------- |
| `seconds`  | General timeout and default is `5` seconds. Note that a function-specific timeout overrides this. |
| `strategy` | `TimeoutStrategy.STOP` (default) or `TimeoutStrategy.CONTINUE`.                                   |

### Options for `TimeoutStrategy`

| Option                     | Description                                                         |
| -------------------------- | ------------------------------------------------------------------- |
| `TimeoutStrategy.STOP`     | Default. Fail fast upon timeout and raise errors.                   |
| `TimeoutStrategy.CONTINUE` | Continue despite timeouts and most errors (syntax errors excluded). |

## Example
How to define a general strategy and timeout of 10 seconds for all functions, which we then override to 5 seconds for a specific function:

```python linenums="1" hl_lines="11"
from browserist import Browser, BrowserSettings, TimeoutSettings, TimeoutStrategy

timeout_settings = TimeoutSettings(
    strategy=TimeoutStrategy.CONTINUE,
    seconds=10)

settings = BrowserSettings(timeout=timeout_settings)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    headline = browser.get.text("//h1", timeout=5)
    print(headline)
```
