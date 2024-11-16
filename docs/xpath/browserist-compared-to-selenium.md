---
title: How to Use XPath Compared to Selenium
description: Browserist is a powerful extension to the Selenium framework that makes web scraping and browser automation even easier. Learn how it differs from Selenium.
tags:
    - Tutorial
    - XPath
    - Selenium
---

# Browserist Compared to Selenium
Browserist is an extension to the [Selenium](https://www.selenium.dev) that makes web scraping and browser automation even easier. Since Browserist only uses XPath expressions to target web elements, be aware of the differences in syntax.

## Examples of Syntax Differences
### Get Element by ID
=== "Browserist with XPath"
    ```python title=""
    browser.get.element("//*[@id='lname']")
    ```

=== "Selenium"
    ```python title=""
    driver.find_element(By.ID, "lname")
    ```

=== "Both"
    ```python title=""
    # Browserist with XPath:
    browser.get.element("//*[@id='lname']")

    # Selenium:
    driver.find_element(By.ID, "lname")
    ```

### Get Element by Class
=== "Browserist with XPath"
    ```python title=""
    browser.get.element("//*[@class='information']")
    ```

=== "Selenium"
    ```python title=""
    driver.find_element(By.CLASS_NAME, "information")
    ```

=== "Both"
    ```python title=""
    # Browserist with XPath:
    browser.get.element("//*[@class='information']")

    # Selenium:
    driver.find_element(By.CLASS_NAME, "information")
    ```

### Get Element by XPath
=== "Browserist with XPath"
    ```python title=""
    browser.get.element("//div[@class='information']")
    ```

=== "Selenium"
    ```python title=""
    driver.find_element(By.XPATH, "//div[@class='information']")
    ```

=== "Both"
    ```python title=""
    # Browserist with XPath:
    browser.get.element("//div[@class='information']")

    # Selenium:
    driver.find_element(By.XPATH, "//div[@class='information']")
    ```

## Why Use XPath?
While Selenium offers several methods to target web elements – for instance `By.ID`, `By.CLASS_NAME`, etc. – Browserist solely uses XPath to locate web elements in the DOM of a web page. Why so?

XPath is a simple, yet powerful tool similar to a Swiss Army knife that gets the job done with compact code. And so you only need to master a single vocabulary instead of multiple `By` class options and importing extra modules from Selenium.
