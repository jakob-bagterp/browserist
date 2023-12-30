---
tags:
    - Tutorial
---

# Best Practice for Downloading Files
Instead of using the [`click.button()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.button) method to download files, you get more control with the dedicated [`click.download()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download) and [`click.download_and_get_file_path()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download_and_get_file_path) methods.

Read ahead to learn how to automate file downloads easily and with stability.

## Destination Directory for Downloads
Firstly, ensure you know where files are downloaded. The default is the `Downloads` folder of the user, or you can set a custom download directory in the [`download_dir` parameter of `BrowserSettings`](./settings/overview.md).

It's only possible to set a single download directory for each browser session, not different destinations for different downloads.

!!! note
    Avoid that multiple browser instances have access to the same download directory. As Browserist monitors the download directory for file changes, it may cause unexpected behaviour if multiple files are downloaded to the same directory at the same time.

## Simple Download or Get Path to Downloaded File
You can use two main methods to download files:

| Method | Description |
| ------ | ----------- |
| [`click.download()`](#clickdownload) | Download file as background task or await completion. |
| [`click.download_and_get_file_path()`](#clickdownload_and_get_file_path) | Download file and return the its path after completion. |

### `click.download()`
Simple download of a file, either as a background task or await the download to complete. Options:

| Parameters | Background Task | Benefit | Disadvantage |
| ------ | --------------- | ------- | ------------ |
| `"//xpath/to/button"` | :material-check: | Faster | If the browser quits during a download, the download may be cancelled or left uncomplete |
| ...<br>`await_download=True` | :material-minus: | Stable download as we wait for download to complete | This will attempt to guess the file name, which may be slower |
| ...<br>`expected_file_name="file.zip"` | :material-minus: | Stable download as we wait for download to complete | Slower than background task, yet faster if you know the file name |

Examples in context:

```python title="" linenums="1"
from browserist import Browser

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.click.download("//xpath/to/button")
    browser.click.download("//xpath/to/button", await_download=True)
    browser.click.download("//xpath/to/button", await_download=True, expected_file_name="file.zip")
```

### `click.download_and_get_file_path()`
Use this method to download a file and get its file path once the download is complete. As downloads are automatically handled by the browser, this is useful if you don't know the file name beforehand. Example

```python title="" linenums="1"
from browserist import Browser

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    file_path = browser.click.download_and_get_file_path("//xpath/to/button")
```

The return type is `Path` from the standard [`pathlib`](https://docs.python.org/3/library/pathlib.html) library, and so you can easily get the file name or absolute path. For instance:

```python title="" linenums="6"
    print("File name:", file_path.name)
    # File name: file.zip
    print("Absolute file path:", file_path.absolute())
    # Absolute path: /home/user/downloads/file.zip
```
