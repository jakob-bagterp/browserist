---
title: How to Configure Timeout Strategy
description: Should the browser stop or continue when a function times out or if something breaks? Learn how to set the best timeout strategy for the needs and context of your automation workflow.
tags:
    - Tutorial
    - Settings
---

# Timeout Strategy
What happens if a function times out: Should the browser stop or continue its operation?

Define a general strategy and timeout in seconds:

* Default is `5` seconds per function (note that a function-specific timeout overrides this)
* The strategy can be `TimeoutStrategy.STOP` (default) or `TimeoutStrategy.CONTINUE`

```python linenums="1"
from browserist import Browser, BrowserSettings, TimeoutSettings, TimeoutStrategy

timeout_settings = TimeoutSettings(
    strategy=TimeoutStrategy.CONTINUE,
    seconds=10)

settings = BrowserSettings(timeout=timeout_settings)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

## Strategy Options
| Option                     | Description                                                         |
| -------------------------- | ------------------------------------------------------------------- |
| `TimeoutStrategy.STOP`     | Default. Fail fast upon timeout and raise errors.                   |
| `TimeoutStrategy.CONTINUE` | Continue despite timeouts and most errors (syntax errors excluded). |
