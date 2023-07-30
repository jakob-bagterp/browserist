# XPath Cheatsheet
## Simple Node Selection
### Absolute Expressions
Use absolute XPath expressions to target a single node:

| XPath | Description |
| ----- | ----------- |
| `/html/head/title` | Get the page title node. |
| `/html/body` | Get the `<body>` element. |

### Relative Expressions
Use relative XPath expressions to target multiple nodes:

| XPath | Description |
| ----- | ----------- |
| `//img` | Get all `<img>` image nodes. |
| `//h1` | Get all `<h1>` headline nodes. |

### Indexing
Combine relative XPath expressions with indexing to target specific nodes:

| XPath | Description |
| ----- | ----------- |
| `//ul[1]/li[3]` | Get the third `<li>` child node of the first `<ul>` list. |
| `//ul[1]/li[position()>1]` | Get all `<li>` child nodes of the first `<ul>` list except the first one. |
| `//form[@id='login']/input[3]` | Get the third `<input>` child node of a form with a specific `id`. |
| `//h2[1]//p` | Of the first `<h2>` headline, get any of its child `<p>` paragrapds. |

### Attributes
Get nodes with certain attributes with the `@` selector:

| XPath | Description |
| ----- | ----------- |
| `//div[@class='some_class']` | Get all `<div>` nodes with with a specific `class` attribute. |
| `//*[@id='some_id']` | Get all nodes with the `*` wildcard selector with a specific `id` attribute. |
| `//input[@type="password"]` | Get all `<input>` nodes that are a password type. |

### Parents and Children
As we most often traverse down the hierachy with `/` or `//`, sometimes we need to get parent nodes with `..`:

| XPath | Description |
| ----- | ----------- |
| `//h1/..` | Get the parents of any `<h1>` headline nodes. |
| `//*[@id='some_id']/..` | Get the parent of a node with a specific `id`. |
| `//li[1]/../li[9]` | Combine parents and children to jump to the ninth list element of the first list. |

See more examples in the [axes](#axes) section.

### Several Paths
Use the pipe `|` to combine several paths in union:

| XPath | Description |
| ----- | ----------- |
| `//h2 | //h3` | Get all `<h2>` and `<h3>` headline nodes. |

## Text
When you need just the content of a node, use the `text()` function:

```text title=""
//h1/text()
```

### Exact Matching
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

### Non-Exact Matching
Get all `<h2>` header nodes that contains some text using the `contains()` function:

```text title=""
//h2[contains(text(), 'some text')]
```

Get all submit buttons using the `normalize-space()` function that strips leading and trailing whitespace, including sequences of whitespace characters replaced with a single space. This is useful to target buttons with different text content, yet the same meaning:

```text title=""
//button[normalize-space()='submit']
```

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

Get all blog links that about food using the `and` operator:

```text title=""
//a[contains(@href, 'blog') and contains(@href, 'food')]
```

Get all blog links that are not about food by combining the `and` and `not()` operators:

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

## SEO
Certain XPath expressions are especially useful for search engine optimisatoin (SEO).

### Content
Count all `<h1>` nodes to ensure that a web page has and only has one main headline Should not be 0 or larger than 1:

```text title=""
count(//h1)
```

### Meta Data
Similarly, ensure that a web page has meta description:

```text title=""
count(//meta[@name='description'])
```

Ensure that a web page doesn't have an empty title:

```text title=""
/html/head/title[.!='']
```

Check if a web page has a canonical URL:

```text title=""
count(//link[@rel='canonical'])
```

Ensure that a web page has a robots meta tag:

```text title=""
count(/html/head/meta[@name='robots'])
```

## Axes
