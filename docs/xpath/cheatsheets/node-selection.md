---
title: XPath Cheatsheet for Node Selection
description: Learn how to use poweful XPath methods to target specific nodes or groups. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Cheatsheet
    - XPath
---

# XPath Cheatsheet for How to Select Nodes
## Absolute Expressions
Use absolute XPath expressions to target a single node:

| XPath | Description |
| ----- | ----------- |
| `/html/head/title` | Get the page title node. |
| `/html/body` | Get the `<body>` element. |

## Relative Expressions
Use relative XPath expressions to target multiple nodes:

| XPath | Description |
| ----- | ----------- |
| `//img` | Get all `<img>` image nodes. |
| `//h1` | Get all `<h1>` headline nodes. |

## Indexing
Combine relative XPath expressions with indexing to target specific nodes:

| XPath | Description |
| ----- | ----------- |
| `//ul[1]/li[3]` | Get the third `<li>` child node of the first `<ul>` list. |
| `//ul[1]/li[position()>1]` | Get all `<li>` child nodes of the first `<ul>` list except the first one. |
| `//form[@id='login']/input[3]` | Get the third `<input>` child node of a form with a specific `id`. |
| `//h2[1]//p` | Of the first `<h2>` headline, get any of its child `<p>` paragrapds. |

## Attributes
Get nodes with certain attributes with the `@` selector:

| XPath | Description |
| ----- | ----------- |
| `//div[@class='some_class']` | Get all `<div>` nodes with with a specific `class` attribute. |
| `//*[@id='some_id']` | Get all nodes with the `*` wildcard selector with a specific `id` attribute. |
| `//input[@type="password"]` | Get all `<input>` nodes that are a password type. |

## Parents and Children
Though we most often traverse down the hierachy with `/` or `//`, sometimes we need to get parent nodes with `..`:

| XPath | Description |
| ----- | ----------- |
| `//h1/..` | Get the parent(s) of any `<h1>` headline nodes. |
| `//*[@id='some_id']/..` | Get the parent of a node with a specific `id`. |
| `//li[1]/../li[9]` | Combine parent and children to jump to the ninth list element of the first list. |

See more examples in the [axes](axes.md) section.

## Union of Several Paths
Use the pipe `|` to combine several paths in union:

| XPath | Description |
| ----- | ----------- |
| `//h2 | //h3` | Get all `<h2>` and `<h3>` headline nodes. |
