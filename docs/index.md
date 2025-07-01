---
title: Get Started with Web Scraping & Browser Automation
description: Browserist is the easy way to do web scraping and browser automation with Python and as an extension for the Selenium web driver.
---

[![Latest version](https://img.shields.io/static/v1?label=version&message=1.7.8&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
[![Python 3.11 | 3.12 | 3.13+](https://img.shields.io/static/v1?label=python&message=3.11%20|%203.12%20|%203.13%2B&color=blueviolet)](https://www.python.org)
[![Apache 2.0 license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/browserist/branch/master/graph/badge.svg?token=1JL65T099J)](https://codecov.io/gh/jakob-bagterp/browserist)
[![CodeQL](https://github.com/jakob-bagterp/browserist/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/github-code-scanning/codeql)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/browserist)](https://pepy.tech/project/browserist)

# Browserist – Python Extension for Selenium 👨‍💻
## What is Browserist?
> ***browserist***
> *1. The belief that web browsers account for differences in websites or web applications in all of their ability and that a particular web browser is superior to others.*
> *2. Discrimination or prejudice based on web browser.*

Despite the [urban definition](https://www.urbandictionary.com/define.php?term=browserist), Browserist is a Python extension of the [Selenium web driver](https://www.selenium.dev/) that makes it even easier to use different browsers for testing and automation.

## Key Features
With Browserist as an extension to Selenium, you get:

:white_check_mark: &nbsp;&nbsp;Improved stability and speed

:white_check_mark: &nbsp;&nbsp;Simple syntax and less code

:white_check_mark: &nbsp;&nbsp;Hassle-free setup across browsers: Chrome, Firefox, Edge, Safari, Internet Explorer

:white_check_mark: &nbsp;&nbsp;Extensive framework of functions that makes browser automation easy

:white_check_mark: &nbsp;&nbsp;Efficient development workflow with IntelliSense and type hints

## Example
Imagine you want to fill out a form on a website. Here's how easy it is with Browserist: We open an automated browser session, access the website, fill out the form, and then submit it. The browser will hereafter close automatically:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")

    browser.input.value("//xpath/to/name_field", "My Name")
    browser.input.value("//xpath/to/email_field", "contact@example.com")
    browser.input.value("//xpath/to/phone_field", "123-456-7890")
    browser.input.value("//xpath/to/address_field", "123 Main St, Anytown USA")

    browser.click.button("//xpath/to/submit_button")
```

If you're new to XPath — a powerful query language used to target elements of a web page — don't worry. You can find out more in the [XPath basics tutorial](xpath/basics.md).

## Next Steps
Ready to try? [Let's get started](getting-started/index.md).

For Selenium users, learn more about how [Browserist is different from Selenium](difference-from-selenium.md).

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
