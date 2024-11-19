---
title: How to Target HTML Attributes with XPath
description: Learn powerful XPath expressions to target HTML attributes like @id and @name instead of relying on element position or indexes. Includes code examples.
tags:
    - Tutorial
    - XPath
---

# Tips and Tricks for XPath Expressions
XPath is a powerful tool that allows you to filter and select nodes on an HTML page. The right approach to XPath can make your life even easier when doing web scraping and browser automation.

Find examples for both beginners and advanced users in this section.

## How to Target HTML Attributes
When targeting elements in an HTML document, it's often best to use attributes like `id`, `name`, or `type` to make your XPath expressions more robust. This is especially useful when the HTML layout changes, but the attributes remain constant.

Let's imagine a registration form on a web page where we want to target the `<input>` elements:

```html linenums="1"
<div class="container">
  <form id="registration_form">
    <label for="email">Email</label>
    <input type="text" placeholder="Enter email" name="email" id="email" required />

    <label for="password">Password</label>
    <input type="password" placeholder="Enter password" name="password" id="password" required />

    <label for="password_repeat">Repeat password</label>
    <input type="password" placeholder="Repeat password" name="password_repeat" id="password_repeat" required />

    <button type="submit">Register</button>
  </form>
</div>
```

Instead of targeting the index `//input[1]`, `//input[2]`, etc., we can be more specific and target the `id` attributes:

```text title=""
//input[@id='email']
//input[@id='password']
//input[@id='password_repeat']
```

Similarly, we can also target other attributes like `name`:

```text title=""
//input[@name='email']
```

This will often make your code more stable if the HTML layout changes while the `name` and `id` attributes often remain constant. Similarly, the submit button is easily located by the `type` attribute:

```text title=""
//button[@type='submit']
```

## Example
All in all, how to apply this for web scraping and browser automation using Browserist:

```python linenums="1" hl_lines="5-9"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.input.value("//input[@id='email']", "user_name@example.com")
    browser.input.value("//input[@id='password']", "some_password")
    browser.input.value("//input[@id='password_repeat']", "some_password")
    browser.click.button("//button[@type='submit']")
```
