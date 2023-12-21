---
tags:
    - Tutorial
---

# Best Practice for Downloading Files
Instead of using the [`click.button()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.button) method to download files, you get more control with the dedicated [`click.download()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download) and [`click.download_and_get_file_path()`](../reference/browser/click.md#browserist.browser.click.__main__.ClickDriverMethods.download_and_get_file_path) methods.

Read ahead to learn how to automate file downloads easily and with stability.

## Set Up Destination Directory for Downloads
Firstly, ensure you know where files are downloaded. The default is the `Downloads` folder of the user, or you can set a custom download directory in the [`download_dir` parameter of `BrowserSettings`](./settings/overview.md).

It's only possible to set a single download directory for each browser session, not different destinations for different downloads.

!!! note
    Avoid that multiple browser instances have access to the same download directory. As Browserist monitors the download directory for file changes, it may cause unexpected behaviour if multiple files are downloaded to the same directory at the same time.
