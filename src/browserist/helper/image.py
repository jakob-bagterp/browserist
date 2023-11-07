from PIL import Image  # type: ignore
from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.remote.webelement import WebElement

from ..model.type.path import FilePath


def is_element_loaded(driver: BaseWebDriver, element: WebElement) -> bool:
    """Check if image element is loaded and ready in the DOM."""

    is_image_loaded: bool = driver.execute_script(  # type: ignore
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0;",
        element)
    return is_image_loaded or False


def merge_vertically(image_base: Image, image_add: Image) -> Image:  # type: ignore
    """Merge two images vertically. Assumes both images have the same width. "image_add" will be added below "image_base"."""

    merged_image_width: int = image_base.width
    merged_image_height: int = image_base.height + image_add.height
    merged_image = Image.new("RGB", (merged_image_width, merged_image_height))
    merged_image.paste(image_base, (0, 0))
    merged_image.paste(image_add, (0, image_base.height))
    # Rememeber to close images so we avoid PermissionError on especially Windows when trying to remove temporary files:
    image_base.close()
    image_add.close()
    return merged_image


def open(file_path: str) -> Image:  # type: ignore
    """Open image from file path."""

    return Image.open(file_path)


def save(image: Image, file_path: FilePath) -> Image:  # type: ignore
    """Save image to file path."""

    return image.save(file_path)
