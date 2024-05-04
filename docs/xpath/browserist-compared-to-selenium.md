---
tags:
    - Tutorial
    - XPath
    - Selenium
---

# Browserist Compared to Selenium
Browserist is an extension of the [Selenium](https://www.selenium.dev) framework and offers similar functionality. Since Browserist only uses XPath to target web elements, be aware of the differences in syntax.

## Examples of Syntax Differences
### Get Element by ID
```python title="Browserist with XPath"
browser.get.element("//*[@id='lname']")
```

```python title="Selenium"
driver.find_element(By.ID, "lname")
```

### Get Element by Class
```python title="Browserist with XPath"
browser.get.element("//*[@class='information']")
```

```python title="Selenium"
driver.find_element(By.CLASS_NAME, "information")
```

## Why Use XPath?
While Selenium offers several methods to target web elements – for instance `By.ID`, `By.CLASS_NAME`, etc. – Browserist solely uses XPath to locate web elements in the DOM of a web page. Why so?

XPath is a simple, yet powerful tool similar to a Swiss Army knife that gets the job done with compact code. And so you only need to master a single vocabulary instead of multiple `By` class options and importing extra modules from Selenium.