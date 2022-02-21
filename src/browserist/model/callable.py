from typing import Callable

DriverGetTextCallable = Callable[[object, str], str]

DriverGetBoolCallable = Callable[[object, str | list[object]], bool]
