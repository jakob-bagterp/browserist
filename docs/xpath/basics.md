---
title: XPath Basics for Web Scraping
description: Learn about XPath, a powerful query language that can traverse HTML and XML documents. Includes practical examples of how XPath is used in Browserist for web automation and scraping.
tags:
    - Tutorial
    - XPath
---

# XPath Basics 🔍
XPath is a query language that is used for traversing through not just an HTML document – but also XML, XSLT and other document types. It is used commonly to search particular elements or attributes with matching patterns, and XPath includes over 200 built-in functions.

While we use XPath in context of HTML and Python, it's commonly used in other programming languages like JavaScript, Java, C#, C++, and many more.

## How It's Used in Browserist
XPath is an integral of Browserist to target elements of a web page. For example, we can easily get the text of the first `<h1>` headline element without knowinw its exact location on the page:

```python linenums="1"
text = browser.get.text("//h1[1]")
print(text)
```

Or we can easily input values in a form if we know the `id` attribute of the input field. Again, we don't want to know the exact location of the input field on the page:

```python linenums="1"
browser.input.value("//*[@id='username']", "John Doe")
browser.input.value("//*[@id='password']", "password123")
```

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
