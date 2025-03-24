[![Latest version](https://img.shields.io/static/v1?label=version&message=1.7.5&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
[![Python 3.11 | 3.12 | 3.13+](https://img.shields.io/static/v1?label=python&message=3.11%20|%203.12%20|%203.13%2B&color=blueviolet)](https://www.python.org)
[![Apache 2.0 license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/browserist/branch/master/graph/badge.svg?token=1JL65T099J)](https://codecov.io/gh/jakob-bagterp/browserist)
[![CodeQL](https://github.com/jakob-bagterp/browserist/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/github-code-scanning/codeql)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/browserist)](https://pepy.tech/project/browserist)

# 👩‍💻 Browserist – Python Extension for Selenium 👨‍💻
> **browserist**
> 1. The belief that web browsers account for differences in websites or web applications in all of their ability and that a particular web browser is superior to others.
> 2. Discrimination or prejudice based on web browser.

Despite the [urban definition](https://www.urbandictionary.com/define.php?term=browserist), Browserist is a Python extension of the [Selenium web driver](https://www.selenium.dev/) that makes it even easier to use different browsers for testing and automation.

## Key Features
With Browserist as an extension to Selenium, you get:

* Improved stability and speed
* Simple syntax and less code
* Hassle-free setup across browsers: Chrome, Firefox, Edge, Safari, Internet Explorer
* Extensive framework of functions that makes browser automation easy
* Efficient development workflow with IntelliSense and type hints

## How to Install
Ready to try? With [PyPI](https://pypi.org/project/browserist/):

```shell
pip install browserist
```

Or with [Homebrew](https://brew.sh):

```shell
brew tap jakob-bagterp/browserist
brew install browserist
```

Find more installation details [here](https://jakob-bagterp.github.io/browserist/getting-started/installation/).

## Getting Started
You're now ready to go:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Improved Stability and Less Code
Browserist improves stability with less code compared to standard use of Selenium. As browsers need time to render web pages, especially single-page applications, Selenium is often used with explicit timeouts:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")
driver.implicitly_wait(3)
search_box = driver.find_element(By.XPATH, "//xpath/to/input")
search_button = driver.find_element(By.XPATH, "//xpath/to/button")
search_box.send_keys("Lorem ipsum")
search_button.click()
driver.quit()
```

Browserist does the same with less and cleaner code, yet also with increased stability and without explicit/implicit waits:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.input.value("//xpath/to/input", "Lorem ipsum")
    browser.click.button("//xpath/to/button")
```

## Documentation
Find tutorials, code examples, list of all methods and much more [here](https://jakob-bagterp.github.io/browserist).

## Become a Sponsor 🏅
If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

[Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp)

Thank you for your support! 🙌

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/browserist/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/browserist/issues).
