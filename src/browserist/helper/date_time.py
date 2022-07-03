from datetime import datetime


def get_current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def get_current_time() -> str:
    return datetime.now().strftime("%H.%M.%S")
