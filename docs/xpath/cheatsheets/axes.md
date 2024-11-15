---
title: XPath Cheatsheet for Axes
description: Learn how to use powerful XPath methods to traverse the node tree and query hierarchical relationships. Includes code examples.
tags:
    - Tutorial
    - Cheatsheet
    - XPath
---

# XPath Cheatsheet for Axes
Instead of just traversing down the hierarchy, there are multiple axes to query the node tree. An axis is used when we want to query nodes nearby other node or other hierarchical relationships.

| Axis | Description | Example |
| ---- | ----------- | ------- |
| `ancestor` | Selects all ancestors (parent, grandparent, etc.) of current node. | `//h1/ancestor::*` |
| `ancestor-or-self` | Selects all ancestors (parent, grandparent, etc.) of current node and the current node itself. | `//h1/ancestor-or-self::*` |
| `attribute` | Selects all attributes of current node. | `//h1/attribute::*` |
| `child` | Selects all children of current node. | `//h1/child::*` |
| `descendant` | Selects all descendants (children, grandchildren, etc.) of current node. | `//h1/descendant::*` |
| `descendant-or-self` | Selects all descendants (children, grandchildren, etc.) of current node and the current node itself. | `//h1/descendant-or-self::*` |
| `following` | Selects everything in the document after the closing tag of the current node. | `//h1/following::*` |
| `following-sibling` | Selects all siblings after the current node. | `//h1/following-sibling::*` |
| `namespace` | Selects all namespace nodes of current node. | `//h1/namespace::*` |
| `parent` | Selects the parent of current node. | `//h1/parent::*` or `//h1/..` |
| `preceding` | Selects all nodes that appear before the current node in the document, except ancestors, attribute nodes and namespace nodes. | `//h1/preceding::*` |
| `preceding-sibling` | Selects all siblings before the current node. | `//h1/preceding-sibling::*` |
| `self` | Selects the current node. | `//h1/self::*` or `//h1` |
