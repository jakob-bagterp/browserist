def check_if_is_image_element_loaded(driver: object, element: object) -> bool:
    is_image_loaded = driver.execute_script(
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
        element)
    return is_image_loaded or False
