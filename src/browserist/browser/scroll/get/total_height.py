from ....model.browser.base.driver import BrowserDriver


def get_total_scroll_height(browser_driver: BrowserDriver) -> int:
    driver = browser_driver.get_webdriver()
    script_get_total_scroll_height = """return Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
    );"""
    return int(driver.execute_script(script_get_total_scroll_height))  # type: ignore
