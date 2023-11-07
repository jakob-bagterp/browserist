from collections.abc import Callable
from typing import Any

DriverGetTextCallable = Callable[..., str | None]

DriverGetBoolCallable = Callable[..., bool]

BrowserMethodWith2ArgumentsCallable = Callable[[object, str], None]

BrowserMethodWith3ArgumentsCallable = Callable[[object, str, Any], None]

BrowserMethodWith4ArgumentsCallable = Callable[[object, str, Any, Any], None]

BrowserMethodWith5ArgumentsCallable = Callable[[object, str, Any, Any, Any], None]

TimeoutShouldContinueCallable = Callable[[], bool]
