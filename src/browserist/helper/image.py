from PIL import Image


def is_element_loaded(driver: object, element: object) -> bool:
    """Check if image element is loaded and ready in the DOM."""

    is_image_loaded: bool = driver.execute_script(  # type: ignore
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
        element)
    return is_image_loaded or False


def merge_vertically(image_base: Image, image_add: Image) -> Image:  # type: ignore
    """Merge two images vertically. Assumes both images have the same width. "image_add" will be added below "image_base"."""

    merged_image_width: int = image_base.width  # type: ignore
    merged_image_height: int = image_base.height + image_add.height  # type: ignore
    merged_image = Image.new("RGB", (merged_image_width, merged_image_height))
    merged_image.paste(image_base, (0, 0))  # type: ignore
    merged_image.paste(image_add, (0, image_base.height))  # type: ignore
    return merged_image  # type: ignore
