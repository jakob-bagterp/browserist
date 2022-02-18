from typing import Callable, List

DriverGetTextCallable = Callable[[object, str], str]

DriverGetBoolCallable = Callable[[object, str | List[object]], bool]
