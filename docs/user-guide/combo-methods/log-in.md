---
tags:
    - Tutorial
    - Settings
    - Combo
---

# Log In Combo Method
Imagine that you have to automate tests of a web application that requires you to log in. Sometimes you want to ensure that multiple user roles can log in and do certains tasks. You can use the log in combo method and settings classes `LoginForm1Step`, `LoginForm2Steps`, and `LoginCredentials` to do this at scale.

!!! note
    Most websites process login in either one or two steps.
    Use `LoginForm1Step` when username and password are prompted on the same page.
    Use `LoginForm2Steps` when username is prompted first, and then the option to input password appears later on the same or a separate page. The two-step variation is often to verify whether a user exists or not before password can be entered (or should be redirected to a registration page).

## Example
```python title=""
from browserist import Browser, LoginForm1Step, LoginCredentials

user_1 = LoginCredentials(
    username = "some_username",
    password = "some_password")

user_2 = LoginCredentials(
    username = "another_username",
    password = "another_password")

login_form = LoginForm1Step(
    url = "https://example.com/login",
    username_input_xpath = "//xpath/to/username_field",
    password_input_xpath = "//xpath/to/password_field",
    submit_button_xpath = "//xpath/to/login_button")

for user in [user_1, user_2]:
    with Browser() as browser:
        browser.combo.log_in(user, login_form)
        assert browser.check_if.does_exist("//xpath/to/element") is True
```
