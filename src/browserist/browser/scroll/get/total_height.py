def get_total_scroll_height(driver: object) -> int:
    script_get_total_scroll_height = """return Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
    );"""
    return int(driver.execute_script(script_get_total_scroll_height))  # type: ignore
