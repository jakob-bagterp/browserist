def tool_execute_script(driver: object, script: str) -> None:
    driver.execute_script(script)  # type: ignore
