from typing import Callable

DriverGetTextCallable = Callable[[object, str], str]

DriverGetBoolCallable = Callable[..., bool]

BrowserMethodWith2ArgumentsCallable = Callable[[object, str], None]
