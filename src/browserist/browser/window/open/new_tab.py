def open_new_tab(driver: object, url: str | None = None) -> None:
    if url:
        # To ensure support across browsers, use JavaScript rather than CTRL + K keys combination.
        driver.execute_script(f"window.open('{url}', '_blank');")
    else:
        driver.switch_to.new_window("tab")

    # TODO: Should the new tab be in focus? Could be an argument, e.g. ... focus_new_tab = False).
