def open_url_in_new_tab(driver: object, url: str) -> None:
    driver.execute_script(f"window.open('{url}', '_blank');")
    # TODO: Should the new tab be in focus? Could be an argument, e.g. ... focus_new_tab = False).
