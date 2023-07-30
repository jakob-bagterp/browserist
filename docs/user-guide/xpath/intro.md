# Introduction to XPath
Browserist is built as an extension to the Selenium framework and offers similar functionality. However, be aware of the differences.

## Why Use XPath?
While Selenium offers several methods to target web elements – for instance `By.ID`, `By.CLASS_NAME`, etc. – Browserist solely uses XPath to locate web elements in the DOM of a web page. Why so?

XPath is a simple, yet powerful tool that similar to a Swiss Army knife gets the job done with compact code. And so you only need to master a single vocabulary instead of multiple `By` class options and importing extra modules from Selenium.

## Syntax Comparison: Selenium vs. Browserist
### Get Element By ID
<div class="grid" markdown>
```python title="Selenium"
driver.find_element(By.ID, "lname")
```

```python title="Browserist with XPath"
browser.get.element("//*[@id='lname']")
```
</div>

### Get Element By Class
<div class="grid" markdown>
```python title="Selenium"
driver.find_element(By.CLASS_NAME, "information")
```

```python title="Browserist with XPath"
browser.get.element("//*[@class='information']")
```
</div>