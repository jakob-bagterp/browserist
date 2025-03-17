from ..model.browser.base.settings import BrowserSettings
from ..model.browser.base.timeout import TimeoutStrategy


def should_continue(settings: BrowserSettings) -> bool:
    return not all([
        settings.timeout._is_timed_out,
        settings.timeout.strategy is TimeoutStrategy.STOP
    ])


def mediate_timeout(settings: BrowserSettings, timeout: float | None) -> float:
    return settings.timeout.seconds if timeout is None else timeout


def mediate_idle_download_timeout(settings: BrowserSettings, timeout: float | None) -> float:
    return settings.timeout.idle_download_seconds if timeout is None else timeout


def set_is_timed_out(settings: BrowserSettings) -> BrowserSettings:
    settings.timeout._is_timed_out = True
    return settings
