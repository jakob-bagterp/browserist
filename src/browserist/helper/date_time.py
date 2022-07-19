from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H.%M.%S")


def get_current_date_and_time() -> tuple[str, str]:
    """Returns current date and time as tuple. Usage:

    date, time = helper.date_time.get_current_date_and_time()"""

    timestamp = get_timestamp()
    timestamp_split = timestamp.split("_")
    return timestamp_split[0], timestamp_split[1]
