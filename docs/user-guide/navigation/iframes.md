---
tags:
    - Tutorial
    - Navigation
---

# Interacting with Iframes
## What Is an Iframe?
An iframe, also known as an _inline frame_, is an element that loads another HTML page within the document. It essentially places another web page within the parent page. Iframes are commonly used for advertising, embedded video, web analytics, and interactive content.

Because iframes are separate documents, they have their own window object. This means that you must navigate to an iframe separately from the parent page and use the iframe root to interact with its content.

## Switching Between Iframes and Web Pages
Basic navigation between iframes and web pages is easy with Browserist. You can use this method to switch to an iframe...

```python title=""
browser.iframe.switch_to("//xpath/to/iframe")
```

... and since Browserist remembers the parent web page, it's easy to go back to the original page using this method:

```python title=""
browser.iframe.switch_to_original_page()
```

Example in context:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.iframe.switch_to("//xpath/to/iframe")
    element_text = browser.get.text("//xpath/to/iframe/element")
    print(element_text)
    browser.iframe.switch_to_original_page()
```

## How to Query Elements Inside an Iframe
Let's imagine a simple web page with an iframe containing a form:

```html title="Parent Page"
<!DOCTYPE html>
<html>
    <head>
        <title>Parent Page</title>
    </head>
    <body>
        <iframe src="./iframe-with-form.html"></iframe>
    </body>
</html>
```

```html title="Iframe with Form"
<!DOCTYPE html>
<html>
    <head>
        <title>Iframe with Form</title>
    </head>
    <body>
        <form>
            <input type="text" name="username" id="username">
            <input type="password" name="password" id="password">
            <button type="submit">Submit</button>
        </form>
    </body>
</html>
```
!!! failure "What Not to Do"
    To interact with the form and button inside the iframe, you can't do anything like this:

    ```python title=""
    browser.click.button("//iframe//button[type='submit']")
    ```

The correct way to interact with iframes is to first switch to the iframe:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.iframe.switch_to("//iframe[1]")
```

And then query the elements inside the iframe, using the iframe as the root:

```python linenums="6"
    browser.input.value("//*[@id='username']", "admin@example.com")
    browser.input.value("//*[@id='password']", "password123")
    browser.click.button("//button[type='submit']")
    browser.iframe.switch_to_original_page()
```
