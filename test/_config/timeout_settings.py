from browserist import TimeoutSettings, TimeoutStrategy

DEFAULT_NO_TIMEOUT = TimeoutSettings(
    strategy=TimeoutStrategy.CONTINUE
)
