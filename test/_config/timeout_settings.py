from browserist import TimeoutSettings, TimeoutStrategy

DEFAULT_CONTINUE = TimeoutSettings(
    strategy=TimeoutStrategy.CONTINUE
)

DEFAULT_STOP = TimeoutSettings(
    strategy=TimeoutStrategy.STOP
)
