---
title: XPath Tutorial for Absolute vs. Relative Expressions
description: Learn how to write efficient XPath expressions for web scraping and test automation. Understand the difference between absolute and relative XPath patterns.
tags:
    - Tutorial
    - XPath
---

# Absolute and Relative XPath Expressions
An XPath expression can be written in two ways:

* **Absolute**: Starts with `/`
* **Relative**: Starts with `//`

For the examples below, let's imagine a simple web page:

```html linenums="1"
<html>
  <body>
    <main>
      <div id="container">
        <h1>Headline</h1>
        <p>This is the body text</p>
      </div>
    </main>
  </body>
</html>
```

## Absolute XPath
To target the `<h1>` headline element with an absolute XPath expression, use this:

```text title=""
/html/body/main/div/h1
```

This is also called a _full XPath_. Most web pages are much more complicated than this, e.g. with containers and other nested elements, and so you end up typing cumbersome, long XPath expressions. Most often you want to avoid absolute XPath expressions and use the relative variation instead.

## Relative XPath
With a relative XPath expression, you can target an `id` attribute or other anchor points to simplify the expression. This also makes it more readable:

```text title=""
//div[@id='container']/h1
```

Or even simpler:

```text title=""
//h1
```

This way, the relative XPath simply searches for all child elements of the root node that matches the condition.

!!! tip "Tip: Use `*` as Wildcard Selector"
    While `//div[@id='container']` targets a `<div>` element with a specific `id`, it's often favourable to use a generic selector. Try using the asterisk `*` in `//*[@id='container']` instead. This is a _wildcard selector_ that targets all element types whether it's a `<div>`, `<h1>`, or any other tag.

## Multiple Conditions in One Expression
Let's imagine a more complicated page with several nested children to `<div id="container">` where we want to click the `<a>` link element:

```html linenums="1"
<main>
  <div id="container">
    <section>
      <h1>Headline</h1>
      <p>This is the body text</p>
      <button>
        <a href="https://example.com">Click me</a>
      </button>
    </section>
  </div>
</main>
```

How do we target the `<a>` link element efficiently?

We can simply use multiple relative statements similar to this pattern `//…//…` in one expression:

```text title=""
//*[@id='container']//a
```
