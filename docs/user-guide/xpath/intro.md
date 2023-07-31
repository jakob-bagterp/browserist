---
tags:
    - Selenium
    - XPath
---

# Introduction to XPath
Browserist is built as an extension to the Selenium framework and offers similar functionality. However, be aware of the differences.

## Why Use XPath?
While Selenium offers several methods to target web elements – for instance `By.ID`, `By.CLASS_NAME`, etc. – Browserist solely uses XPath to locate web elements in the DOM of a web page. Why so?

XPath is a simple, yet powerful tool similar to a Swiss Army knife that gets the job done with compact code. And so you only need to master a single vocabulary instead of multiple `By` class options and importing extra modules from Selenium.

## Syntax Comparison: Selenium vs. Browserist
### Get Element by ID
```python title="Selenium"
driver.find_element(By.ID, "lname")
```

```python title="Browserist with XPath"
browser.get.element("//*[@id='lname']")
```

### Get Element by Class
```python title="Selenium"
driver.find_element(By.CLASS_NAME, "information")
```

```python title="Browserist with XPath"
browser.get.element("//*[@class='information']")
```
