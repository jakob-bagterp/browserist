---
title: XPath Cheatsheet for Text
description: Learn how to use powerful XPath methods to target specific text in nodes. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Cheatsheet
    - XPath
---

# XPath Cheatsheet for Text
When you need just the content of a node, use the `text()` function:

```text title=""
//h1/text()
```

## Exact Matching
Target all `<button>` nodes with a specific text content:

```text title=""
//button[text()='some text']
```

Get all `<p>` nodes that start with placeholder text using the `starts-with()` function:

```text title=""
//p[starts-with(text(), 'Lorem ipsum')]
```

Ensure that all paragraphs end with a dot by getting all `<p>` nodes and combining the `not()` and `ends-with()` functions:

```text title=""
`//p[not(ends-with(text(), '.'))]`
```

## Non-Exact Matching
Get all `<h2>` header nodes that contains some text using the `contains()` function:

```text title=""
//h2[contains(text(), 'some text')]
```

Get all submit buttons using the `normalize-space()` function that strips leading and trailing whitespace, including sequences of whitespace characters replaced with a single space. This is useful to target buttons with different text content, yet the same meaning:

```text title=""
//button[normalize-space()='submit']
```
