---
tags:
    - Tutorial
    - XPath
---

# Target Attributes with XPath
When targeting elements in an HTML document, it's often best to use attributes like `id`, `name`, or `type` to make your XPath expressions more robust. This is especially useful when the HTML layout changes, but the attributes remain constant.

Let's imagine a registration form on a web page where we want to target the `<input>` elements:

```html linenums="1"
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
