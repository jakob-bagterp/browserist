from typing import Any, Callable

DriverGetTextCallable = Callable[..., str]

DriverGetBoolCallable = Callable[..., bool]

BrowserMethodWith2ArgumentsCallable = Callable[[object, str], None]

BrowserMethodWith3ArgumentsCallable = Callable[[object, str, Any], None]

BrowserMethodWith4ArgumentsCallable = Callable[[object, str, Any, Any], None]

BrowserMethodWith5ArgumentsCallable = Callable[[object, str, Any, Any, Any], None]
