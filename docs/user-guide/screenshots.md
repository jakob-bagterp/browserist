---
tags:
    - Tutorial
---

# How to Automate Screenshots
Screenshots are useful for capturing and documenting the visual appearance of a web page. By automating the process, we can save time and ensure consistency when capturing screenshots across browsers and devices.

## Settings
### Global Destination
You can set the directory where the screenshots are saved by customizing the `screenshot_dir` parameter of the `BrowserSettings`. For example:

```python title="" linenums="1"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(screenshot_dir="/path/to/screenshots")

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.screenshot.visible_portion()
```

!!! info
    By default, screenshots are saved in the `Downloads` folder of the user.

### Override Destination Locally
Or you can override the global settings for a specific screenshot each time you take a screenshot. Simply add the `destination_dir` parameter to the screenshot method:

```python title=""
browser.screenshot.visible_portion(destination_dir="./screenshots")
```

### Custom File Naming
You can customize the name of the screenshot file each time you take a screenshot. For example:

```python title=""
browser.screenshot.visible_portion("image.png")
```

Or combine custom file naming with a custom destination directory:

```python title=""
browser.screenshot.complete_page("image.png", "./screenshots")
```

!!! note
    When setting a custom file name, screenshots should always be saved as a PNG file with a `.png` extension.

## Different Types of Screenshots
### Visible Portion
How to capture the visible portion of a web page, i.e. the current viewport:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.screenshot.visible_portion()
```

### Element
You can also take screenshots of a specific element on a web page:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.screenshot.element("//xpath/to/element")
```

### Complete Page
To capture the entire page, including parts that are not currently visible in the viewport, Browserist scrolls the page programmatically and takes multiple screenshots, which are then stitched together to create a full-page screenshot:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.screenshot.complete_page()
```

!!! note "Firefox Is Recommended for Complete Page Screenshots"
    Firefox is recommended browser for complete page screenshots as it executes this in one go. Other browsers can't capture the entire page at once, and so we need to merge screenshots portion by portions – and this is obviously much slower. For example:

    ```python linenums="1"
    from browserist import Browser, BrowserSettings, BrowserType

    settings = BrowserSettings(browser_type=BrowserType.FIREFOX)

    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.screenshot.complete_page()
    ```
