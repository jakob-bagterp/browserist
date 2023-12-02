---
tags:
    - Tutorial
    - Settings
    - Combo
---

# Log In Combo Method
Imagine that you have to automate tests of a web application that requires you to log in. Sometimes you want to ensure that multiple user roles can log in and do certains tasks. You can use the log in combo method and settings classes `LoginForm1Step`, `LoginForm2Steps`, and `LoginCredentials` to do this at scale.

## One or Two Steps to Log In
Most websites process login in either one or two steps. This often means that the username and password fields are either on the same page or on separate pages.

Use `LoginForm1Step` when username and password are prompted on the same page.

Use `LoginForm2Steps` when username is prompted first, and then the option to input password appears later on the same or a separate page. The two-step variation is often to verify whether a user exists or not before password can be entered (or should be redirected to a registration page).

As `LoginCredentials` is independent of the login form, it works with both options.

| Class | Step 1 | Step 2 | Post Login |
| ----- | ------ | ------ | ---------- |
| `LoginForm1Step` | Input username and password. Then click submit. | | [Multiple options](../../reference/browser/combo/log-in.md#loginform1step) to await confirmation or redirect. |
| `LoginForm2Steps` | Input username and click submit. | Input password and click submit. | [Multiple options](../../reference/browser/combo/log-in.md#loginform2steps) to await confirmation or redirect. |

## Examples
```python linenums="1"
from browserist import Browser, LoginForm1Step, LoginCredentials

user_admin = LoginCredentials(
    username = "admin",
    password = "admin_password")

user_author = LoginCredentials(
    username = "author",
    password = "author_password")

login_form = LoginForm1Step(
    url = "https://example.com/login",
    username_input_xpath = "//xpath/to/username_field",
    password_input_xpath = "//xpath/to/password_field",
    submit_button_xpath = "//xpath/to/login_button")
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
