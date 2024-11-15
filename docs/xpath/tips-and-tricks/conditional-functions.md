---
title: How to Use Conditional XPath Functions
description: Learn powerful XPath expressions to target elements with specific content. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - XPath
---

# How to Use Conditional XPath Functions
## Match Elements with Specific Text
Sometimes you can't use attributes to easily target elements. A calendar is a good example of this. Let's imagine we want to select the first day of a given month:

```html linenums="1"
<div class="calendar">
  <div class="previous">&lt;<div>
  <div class="month">
    June 2023
  </div>
  <div class="next">&gt;<div>

  <ul class="weekdays">
    <li>Mo</li>
    <li>Tu</li>
    <li>We</li>
    <li>Th</li>
    <li>Fr</li>
    <li>Sa</li>
    <li>Su</li>
  </ul>

  <ul class="dates">
    <li class="previous_month">29</li>
    <li class="previous_month">30</li>
    <li class="previous_month">31</li>
    <li>1</li>
    <li>2</li>
    <li class="today">3</li>
    <li>4</li>
    ...
    <li>29</li>
    <li>30</li>
    <li class="next_month">1</li>
    <li class="next_month">2</li>
  </ul>
</div>
```

We can locate June 1 by using by indexing `<li>1</li>` as the fourth date element: `//ul[@class='dates']/li[4]`. But what happens in July, August, etc. when the first day of the month isn't a Thursday?

Let's instead use a _conditional function_ for XPath:

```text title=""
//ul[@class='dates']/li[text()='1']
```

The `…/li[text()='1']` part will return the first exact text match of `1` (and ignore any later matches).

If you want to select other dates, why not create a function in Python that dynamically generates the XPath expression for you?

```python linenums="1"
def get_xpath_for_calendar_date(date: int) -> str:
    return f"//ul[@class='dates']/li[text()='{date}']"
```

!!! tip Exact Matches or Contains Text
    While the `…/li[text()='1']` method locates the first exact match of `1`, it's sometimes favourable to locate the first non-exact match with either the `…/li[contains(text(), '1')]` or `…/li[normalize-space()='1']`  methods as they handle eventual white space more graceful. Despite the differences, all of these conditional methods would yield the correct answer in the calendar case.

Learn more [pattern matching techniques for text](./../cheatsheets/text.md) or tips for [node selection](./../cheatsheets/node-selection.md) in the XPath cheatsheets section.
