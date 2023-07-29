# XPath Basics
## Absolute vs. Relative
An XPath expression can be written in two ways:

* **Absolute**: Starts with `/`
* **Relative**: Starts with `//`

For the examples below, let's imagine a simple web page:

```html
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

### Absolute XPath
To target the `<h1>` headline element with an absolute XPath expression, use this:

```text title=""
/html/body/main/div/h1
```

Most web pages or much more complicated that this with containers and several other, and so you often type cumbersome, long XPath expressions. Most often you want to avoid absolute XPath expressions.

### Relative XPath
With a relative XPath expression, you can target an `id` attribute or other anchor points to simplify the expression. This also makes it more readable:

```text title=""
//*[@id='container']/h1
```

What does `*` mean? This is a _wildcard_ that targets all elements whether it's a `<div>`, `<h1>` or any other tag.

Sometimes even simply:

```text title=""
//h1
```

### Multiple Relative Expressions in One
Let's imagine a more complicated page with several nested children to `<div id="container">`:

```html
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

How do we target the `<a>` link element efficiently? We can simply use multiple relative statements similar to this pattern `//…//…` in one expression:

```text title=""
//*[@id='container']//a
```
