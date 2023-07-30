# XPath Cheatsheet
## Search Engine Optimisation (SEO)
Certain XPath expressions are especially useful for search engine optimisation.

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
