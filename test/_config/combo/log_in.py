import keyring

from browserist import LoginCredentials, LoginForm2Steps

AMAZON_LOGIN_CREDENTIALS = LoginCredentials(
    username=keyring.get_password("browserist-test-amazon-username", "username"),
    password=keyring.get_password("browserist-test-amazon-password", "password"),
)

AMAZON_LOGIN_FORM = LoginForm2Steps(
    username_input_xpath="//*[@id='ap_email']",
    username_submit_button_xpath="//*[@id='continue']",
    password_input_xpath="//*[@id='ap_password']",
    password_submit_button_xpath="//*[@id='signInSubmit']",
    url="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
    post_login_url="https://www.amazon.com/?ref_=nav_signin&",
)
