[![Latest version](https://img.shields.io/static/v1?label=version&message=0.1.2&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
![Python >=3.9](https://img.shields.io/static/v1?label=python&message=>=3.10&color=blueviolet)
[![MIT license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)

# 👩‍💻 Browserist Extension for Selenium 👨‍💻
Extend the Python version of the Selenium web driver with Browserist and make your browser automation even easier.

Main features of Browserist:

* Improves stability and speed
* Extended library of browser automation functions and tools
* Hassle-free setup that works across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer

## Prerequisites
* Python 3.10 or higher
* [Selenium](https://www.selenium.dev)
* Relevant browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer

## Installation
### PyPI
```shell
pip3 install browserist
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, use this terminal command to tap Browserist:

```shell
brew tap jakob-bagterp/browserist
```

And then install:

```shell
brew install browserist
```

## Getting Started
The default browser is Chrome.

```python
from browserist import Browser

browser = Browser()
browser.open.url("http://example.com/")
browser.quit()
```

### Browser Types
If you want to use other browser types, e.g. Firefox, Edge, etc., define this in the settings:

```python
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type = BrowserType.FIREFOX)
browser = Browser(settings)
browser.open.url("http://example.com/")
browser.quit()
```

#### Supported Browsers
| Name              | Type                            |
| ----------------- | ------------------------------- |
| Chrome            | `BrowserType.CHROME`            |
| Edge              | `BrowserType.EDGE`              |
| Firefox           | `BrowserType.FIREFOX`           |
| Internet Explorer | `BrowserType.INTERNET_EXPLORER` |
| Opera             | `BrowserType.OPERA`             |
| Safari            | `BrowserType.SAFARI`            |

### Navigation
Similar to Selenium, use simple commands to automate the browser:

| Action  | How                 | Description                        |
| ------- | ------------------- | ---------------------------------- |
| Forward | `browser.forward()` | Press the browser's back button    |
| Back    | `browser.back()`    | Press the browser's forward button |
| Refresh | `browser.refresh()` | Refresh the current page           |
| Quit    | `browser.quit()`    | Close the browser                  |
