---
tags:
    - Tutorial
---

# Best Practice for Downloading Files
Instead of using the [`click.button()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.button) method to download files, you get more control with the dedicated [`click.download()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download) and [`click.download_and_get_file_path()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download_and_get_file_path) methods.

Read on to learn how to automate file downloads in an easy and stable way.

## Destination Directory for Downloads
First, make sure you know where files are downloaded to. The default is the user's `Downloads` folder, or you can set a custom download directory in the [`download_dir` parameter of `BrowserSettings`](./settings/overview.md).

```python title="" linenums="1"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(download_dir = "/my/downloads")

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.click.download("//xpath/to/button")
```

!!! note
    It's only possible to set a single download directory for each browser session, not different destinations for different downloads.

    Avoid that multiple browser instances have access to the same download directory. As Browserist monitors the download directory for file changes, it may cause unexpected behaviour if multiple files are downloaded to the same directory at the same time.

## Methods
There are two main methods you can use to download files:

| Method | Description |
| ------ | ----------- |
| [`click.download()`](#simple-download) | Download file as background task or await completion |
| [`click.download_and_get_file_path()`](#get-path-to-downloaded-file) | Download file and return its path after completion |

### Simple Download
Use the `click.download()` method for simple file downloads, either as a background task or await the download to complete. Options:

| Parameters | Background Task | Advantage | Disadvantage |
| ------ | --------------- | ------- | ------------ |
| `"//xpath/to/button"` | :material-check: | Faster | If the browser quits during a download, the download may be cancelled or left uncomplete |
| ...<br>`await_download=True` | :material-close: | Stable download as we wait for download to complete | This will attempt to guess the file name, which may be slower |
| ...<br>`expected_file_name="file.zip"` | :material-close: | Stable download as we wait for download to complete | Slower than background task, yet faster if you know the file name |

Examples in context:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.download("//xpath/to/button")
    browser.click.download("//xpath/to/button", await_download=True)
    browser.click.download("//xpath/to/button", await_download=True, expected_file_name="file.zip")
```

### Get the Path to the Downloaded File
Use the `click.download_and_get_file_path()` method to download a file and get its file path once the download is complete. As downloads are handled automatically by the browser, this is useful if you don't know the file name beforehand. For example:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    file_path = browser.click.download_and_get_file_path("//xpath/to/button")
```

The return type is `Path` from the standard [`pathlib`](https://docs.python.org/3/library/pathlib.html) library, and so you can easily get the file name or absolute path. For instance:

```python title="" linenums="6"
    print(file_path.name)
    # file.zip
    print(file_path.absolute())
    # /home/user/downloads/file.zip
```
