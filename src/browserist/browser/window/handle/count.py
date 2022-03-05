from .all import get_all_window_handles


def count_window_handles(driver: object) -> int:
    return len(get_all_window_handles(driver))
