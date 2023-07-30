---
tags:
    - Tutorial
    - XPath
---

# XPath Cheatsheet
## Links
Combine attributes and functions to target specific link nodes. But first, how to get all `<a>` link nodes:

```text title=""
//a
```

### Exact Matching
Get all HTTPS links using the `starts-with()` function:

```text title=""
//a[starts-with(@href, 'https')]
```

Get all non-HTTPS links. As above but negated by the `non()` function:

```text title=""
//a[not(starts-with(@href, 'https'))]
```

Get all links for MP3 audio files using the `ends-with()` function:

```text title=""
//a[ends-with(@href, '.mp3')]
```

Get all links without a trailing slash by combining the `not()` and `ends-with()` functions.

```text title=""
//a[not(ends-with(@href, '/'))]
```

### Non-Exact Matching
Get all blog links that using the `contains()` function:

```text title=""
//a[contains(@href, 'blog')]
```

Negate the above to get all non-blog links using the `not()` function:

```text title=""
//a[not(contains(@href, 'blog'))]
```

Get all blog links about food using the `and` operator:

```text title=""
//a[contains(@href, 'blog') and contains(@href, 'food')]
```

Get all blog links that aren't about food by combining the `and` and `not()` operators:

```text title=""
//a[contains(@href, 'blog') and not(contains(@href, 'food'))]
```

Get all blog or news links using the `or` operator:

```text title=""
//a[contains(@href, 'blog') or contains(@href, 'news')]
```

### Other
Get all links with a URL longer than 55 characters using the `string-length()` function:

```text title=""
//a[string-length(@href) > 55]
```
