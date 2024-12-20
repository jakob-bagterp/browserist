---
title: XPath Cheatsheet for Search Engine Optimisation
description: Learn how to use powerful XPath methods to ensure that a web page has relevant meta data to improve SEO. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Cheatsheet
    - XPath
---

# XPath Cheatsheet for Search Engine Optimisation (SEO)
Certain XPath expressions are especially useful for search engine optimisation.

## Content
### H1 Headline
Count all `<h1>` nodes to ensure that a web page has and only has one main headline. Should not be 0 or larger than 1:

```text title=""
count(//h1)
```

???+ example
    How to use Browserist to check whether a web page has exactly one `<h1>` headline tag:

    ```python linenums="1" hl_lines="5"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        assert browser.tool.count_elements("//h1") == 1
    ```

### Image Alt Text
Ensure that all images on web page have an alt text.

```text title=""
//img[not(@alt)]
```

???+ example
    How to use Browserist to check whether a web page has images without alt text:

    ```python linenums="1" hl_lines="5-9"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        if browser.check_if.does_exist("//img"):
            alt_texts = browser.get.attribute.values("//img", "alt")
            for alt_text in alt_texts:
                assert len(alt_text) > 0
    ```

## Meta Data
Similarly, ensure that a web page has meta description. Should not be 0 or larger than 1:

```text title=""
count(//meta[@name='description']/@content)
```

And you can ensure that length of the meta description is between 50 and 160 characters by using the `string-length()` function:

```text title=""
string-length(/html/head/meta[@name='description']/@content) >= 50
string-length(/html/head/meta[@name='description']/@content) <= 160
```

Check if a web page has a canonical URL. If it has, it should only be 1:

```text title=""
count(//link[@rel='canonical'])
```

Ensure that a web page has a robots meta tag. Should not be 0 or larger than 1:

```text title=""
count(//meta[@name='robots'])
```

???+ example
    How to use Browserist to check whether a web page has relevant meta data:

    ```python linenums="1" hl_lines="7 9 12"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")

        if browser.check_if.does_exist("//link[@rel='canonical']"):
            assert browser.tool.count_elements("//link[@rel='canonical']") <= 1

        assert browser.tool.count_elements("//meta[@name='robots']") == 1

        meta_description = browser.get.attribute.value("//meta[@name='description']", "content")
        assert 50 <= len(meta_description) <= 160
    ```

## Page Title
Ensure that a web page doesn't have an empty title:

```text title=""
/html/head/title[. != '']
```

???+ example
    How to use Browserist to check whether a web page has a page title:

    ```python linenums="1" hl_lines="5"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        assert browser.check_if.does_exist("/html/head/title[. != '']")
    ```

    Alternatively, there's a simpler solution without using XPath:

    ```python linenums="5" hl_lines="1"
        assert browser.get.page_title() != ""
    ```
