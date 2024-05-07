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

!!! note
    When setting a custom file name, screenshots should always be saved as a PNG file with a `.png` extension.
