from datetime import datetime


def default_file_name() -> str:
    """Example: \"Browserist screenshot 2022-02-12 at 22.12.34.png\""""

    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H.%M.%S")
    return f"Browserist screenshot {date} at {time}.png"
