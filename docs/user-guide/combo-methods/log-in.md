---
title: How to Log In with User Profiles in Web Scraping
description: Learn how to automate login and user profiles using combo methods in Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Settings
    - Combo
---

# How to Handle Logins and User Profiles
Imagine that you have to automate tests of a web application that requires you to log in. Sometimes you want to ensure that multiple user roles can log in and do certains tasks.

You can use the log in combo method and settings classes `LoginForm1Step`, `LoginForm2Steps`, and `LoginCredentials` to do this at scale.

## One or Two Steps to Log In
Most websites process login in either one or two steps. This often means that the username and password fields are either on the same page or on separate pages.

Use `LoginForm1Step` when username and password are prompted on the same page.

Use `LoginForm2Steps` when username is prompted first, and then the option to input password appears later on the same or a separate page. The two-step variation is often to verify whether a user exists or not before password can be entered (or should be redirected to a registration page).

As `LoginCredentials` is independent of the login form, it works with both options.

| Class             | Step 1                                          | Step 2                           | Post Login                                                                                                     |
| ----------------- | ----------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `LoginForm1Step`  | Input username and password. Then click submit. | –                                | [Multiple options](../../reference/browser/combo/log-in.md#loginform1step) to await confirmation or redirect.  |
| `LoginForm2Steps` | Input username and click submit.                | Input password and click submit. | [Multiple options](../../reference/browser/combo/log-in.md#loginform2steps) to await confirmation or redirect. |

## Examples
### Basic Usage
Getting started:

```python linenums="1"
from browserist import Browser, LoginForm1Step, LoginCredentials

login_credentials = LoginCredentials(
    username="some_username",
    password="some_password")

login_form = LoginForm1Step(
    url="https://example.com/login",
    username_input_xpath="//xpath/to/username_field",
    password_input_xpath="//xpath/to/password_field",
    submit_button_xpath="//xpath/to/login_button")

with Browser() as browser:
    browser.combo.log_in(login_credentials, login_form)
    browser.open.url("https://example.com/some_page")
    browser.click.button("//xpath/to/button")
```

### Conditional Flows
Sometimes it's useful to let a flow be dependent of succesfull handling of the login form. This is possible by setting `return_bool` to `True` as parameter in the settings class and using a conditional `if` statement in combination with the login combo. For example:

```python linenums="1"
from browserist import Browser, LoginForm1Step, LoginCredentials

login_credentials = LoginCredentials(
    username="some_username",
    password="some_password")

login_form = LoginForm1Step(
    url="https://example.com/login",
    username_input_xpath="//xpath/to/username_field",
    password_input_xpath="//xpath/to/password_field",
    submit_button_xpath="//xpath/to/login_button",
    post_login_url_contains="https://example.com/successfull_logged_in_page",
    post_login_element_xpath="//xpath/to/successfull_logged_in_element",
    return_bool=True)

with Browser() as browser:
    if browser.combo.log_in(login_credentials, login_form):
        browser.open.url("https://example.com/some_page")
        browser.click.button("//xpath/to/button")
```

### Testing Purposes
Let's expand the example and imagine that a website can be personalised based on which user role is signed in. For instance, we want to ensure that only the admin role has visible access to an administration module.

Firstly, let's define the settings classes:

```python linenums="1"
from browserist import Browser, LoginForm1Step, LoginCredentials

user_admin = LoginCredentials(
    username="admin",
    password="admin_password")

user_author = LoginCredentials(
    username="author",
    password="author_password")

login_form = LoginForm1Step(
    url="https://example.com/login",
    username_input_xpath="//xpath/to/username_field",
    password_input_xpath="//xpath/to/password_field",
    submit_button_xpath="//xpath/to/login_button")
```

After the the settings classes are defined, let's attempt to log both users in:

```python title="" linenums="17"
for user in [user_admin, user_author]:
    with Browser() as browser:
        browser.combo.log_in(user, login_form)
        assert browser.check_if.does_exist("//xpath/to/validation_element") is True
```

Hereafter, let's imagine that we want ensure that only the admin role has visible access to an administration module:

```python title="" linenums="22"
        browser.open.url("https://example.com/backoffice")
        admin_module_display_status = browser.check_if.is_displayed("//xpath/to/admin_module")
        if user is user_admin:
            assert admin_module_display_status is True
        else:
            assert admin_module_display_status is False
```
