from typing import Any, Callable

DriverGetTextCallable = Callable[[object, str], str]

DriverGetBoolCallable = Callable[..., bool]

BrowserMethodWith2ArgumentsCallable = Callable[[object, str], None]

BrowserMethodWith3ArgumentsCallable = Callable[[object, str, Any], None]

BrowserMethodWith4ArgumentsCallable = Callable[[object, str, Any, Any], None]
