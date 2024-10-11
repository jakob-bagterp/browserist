---
tags:
    - Tutorial
---

# How to Get the HTML Source
Sometimes it's useful to get the HTML source of a page or specific elements. With Browserist, that's easily done.

For the following examples, let's imagine the following boilerplate page source:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example.com</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

## Page Source
How to get all the HTML source of a page:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    page_source = browser.get.html.page_source()
    print(page_source)
```

This will print the full page source as above:

```html
<!DOCTYPE html>
<html lang="en">
    ...
</html>
```

## Source by Element
### Inner HTML
How to get the inner HTML source of an element:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    inner_html = browser.get.html.element_inner("//body")
    print(inner_html)
```

This will give you the inner HTML of the `<body>` tag:

```html
<h1>Welcome</h1>
<p>This is a paragraph.</p>
```

### Outer HTML
How to get the outer HTML source of an element:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    outer_html = browser.get.html.element_outer("//body")
    print(outer_html)
```

This will give you the outer HTML of the `<body>` tag:

```html
<body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
</body>
```
