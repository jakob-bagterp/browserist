---
tags:
    - Tutorial
---

# How to Count Elements
Sometimes it's useful to count the elements of a specific selector, either to check whether the expected number of elements are present, or to automate an iteration over them.

## Use Case for Counting Search Results
For instance, you may want to know how many search results are displayed on a search engine result page:

```python linenums="1"
from browserist import Browser

search_term = "test"
search_results_xpath = "//*[@class='search-result-item']"

with Browser() as browser:
    browser.open.url(f"https://www.search.com/web?q={search_term}")
    number_of_results = browser.tool.count_elements(search_results_xpath)
    if number_of_results > 0:
        for i in range(1, number_of_results + 1):
            search_result_text = browser.get.text(f"{search_results_xpath}[{i}]")
            print(f"Search result {i}: {search_result_text}")
    else:
        print("No search results found.")
```

## Other Examples
### Images
How to count the number of `<img>` image elements on a page:

```python title=""
number_of_images = browser.tool.count_elements("//img")
```

### Links
How to count the number of `<a>` link elements on a page:

```python title=""
number_of_links = browser.tool.count_elements("//a")
```

### Headlines
How to count the number of `<h1>` headline elements on a page:

```python title=""
number_of_headlines = browser.tool.count_elements("//h1")
```

### Paragraphs
How to count the number of `<p>` paragraph elements on a page:

```python title=""
number_of_paragraphs = browser.tool.count_elements("//p")
```
