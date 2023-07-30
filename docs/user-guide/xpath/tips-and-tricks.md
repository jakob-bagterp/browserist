---
tags:
    - Tutorial
    - XPath
---

# Tips and Tricks for XPath Expressions
The right approach to XPath can make your life even easier as a browser automater. Let's take a few examples from intermediate to advanced level.

## Target Attributes
Let's imagine a registration form on a web page where we want to target the `<input>` elements:

```html
<div class="container">
  <form id="registration_form">
    <label for="email">Email</label>
    <input type="text" placeholder="Enter email" name="email" id="email" required />

    <label for="password">Password</label>
    <input type="password" placeholder="Enter password" name="password" id="password" required />

    <label for="password_repeat">Repeat password</label>
    <input type="password" placeholder="Repeat password" name="password_repeat" id="password_repeat" required />

    <button type="submit">Register</button>
  </form>
</div>
```

Instead of targeting the index `//input[1]`, `//input[2]`, etc., we can be more specific and target the `id` attributes:

```text title=""
//input[@id='email']
//input[@id='password']
//input[@id='password_repeat']
```

Similarly, we can also target other attributes like `name`:

```text title=""
//input[@name='email']
```

This will often make your code more stable if the HTML layout changes while the `name` and `id` attributes often remain constant. Similarly, the submit button is easily located by the `type` attribute:

```text title=""
//button[@type='submit']
```

## Conditional Functions
### Match Elements with Specific Text
Sometimes you can't use attributes to easily target elements. A calendar is a good example of this. Let's imagine we want to select the first day of a given month:

```html
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

```python
def get_xpath_for_calendar_date(date: int) -> str:
    return f"//ul[@class='dates']/li[text()='{date}']"
```

!!! tip Exact Matches or Contains Text
    While the `…/li[text()='1']` method locates the first exact match of `1`, it's sometimes favourable to locate the first non-exact match with the `…/li[contains(text(), '1')]` method. Despite the difference, either of the conditional methods would yield the correct answer in the calendar case.
