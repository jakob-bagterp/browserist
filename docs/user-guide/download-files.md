---
title: How to Download Files
description: Learn how to download files with Browserist, either as background task or await completion. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
---

# How to Download Files
## Best Practice for Browser Automation
Instead of using the [`click.button()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.button) method to download files, you get more control with the dedicated [`click.download()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download) and [`click.download_and_get_file_path()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download_and_get_file_path) methods.

Read on to learn how to automate file downloads in an easy and stable way.

## Destination Directory for Downloads
First, make sure you know where files are downloaded to. The default is the user's `Downloads` folder, or you can set a custom download directory in the [`download_dir` parameter of `BrowserSettings`](../settings/overview.md).

```python linenums="1" hl_lines="3 7"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(download_dir="/my/downloads")

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.click.download("//xpath/to/button")
```

!!! note
    It's only possible to set a single download directory for each browser session, not different destinations for different downloads.

    Avoid that multiple browser instances have access to the same download directory. As Browserist monitors the download directory for file changes, it may cause unexpected behaviour if multiple files are downloaded to the same directory at the same time.

## Methods
There are two main methods you can use to download files:

| Method                                                                       | Description                                          |
| ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| [`click.download()`](#simple-download)                                       | Download file as background task or await completion |
| [`click.download_and_get_file_path()`](#get-the-path-to-the-downloaded-file) | Download file and return its path after completion.  |

### Simple Download
Use the `click.download()` method for simple file downloads, either as a background task or await the download to complete. Options:

<div id="download-methods-table"></div>

| Parameters                             | Background Task  | Advantage                                           | Disadvantage                                                                            |
| -------------------------------------- | ---------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `//xpath/to/button`                    | :material-check: | Faster                                              | If the browser closes during a download, the download may be aborted or left incomplete |
| ...<br>`await_download=True`           | :material-close: | Stable download as we wait for download to complete | This will attempt to guess the file name, which may be slower                           |
| ...<br>`expected_file_name="file.zip"` | :material-close: | Stable download as we wait for download to complete | Slower than background task, yet faster if you know the file name                       |

Examples in context:

```python linenums="1" hl_lines="5-7"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.download("//xpath/to/button")
    browser.click.download("//xpath/to/button", await_download=True)
    browser.click.download("//xpath/to/button", await_download=True, expected_file_name="file.zip")
```

### Get the Path to the Downloaded File
Use the `click.download_and_get_file_path()` method to download a file and get its file path once the download is complete. As downloads are handled automatically by the browser, this is useful if you don't know the file name beforehand. For example:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    file_path = browser.click.download_and_get_file_path("//xpath/to/button")
```

The return type is `Path` from the standard [`pathlib`](https://docs.python.org/3/library/pathlib.html) library, and so you can easily get the file name or absolute path.

For instance, this will output the file name `file.zip` in the terminal:

```python title="" linenums="6"
    print(file_path.name)
```

And this will output the absolute file path `/home/user/downloads/file.zip` in the terminal:

```python title="" linenums="7"
    print(file_path.absolute())
```
