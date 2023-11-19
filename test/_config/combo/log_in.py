from _mock_data.url import internal_url

from browserist import LoginCredentials, LoginForm1Step, LoginForm2Steps

VALID_USERNAME = "johndoe"

VALID_PASSWORD = "password123"

INVALID = "invalid"

LOGIN_CREDENTIALS_VALID = LoginCredentials(
    username=VALID_USERNAME,
    password=VALID_PASSWORD,
)

LOGIN_CREDENTIALS_INVALID = LoginCredentials(
    username=INVALID,
    password=INVALID,
)

LOGIN_CREDENTIALS_INVALID_USERNAME = LoginCredentials(
    username=INVALID,
    password=VALID_PASSWORD,
)

LOGIN_CREDENTIALS_INVALID_PASSWORD = LoginCredentials(
    username=VALID_USERNAME,
    password=INVALID,
)

USERNAME_INPUT_XPATH = "//*[@id='username']"

PASSWORD_INPUT_XPATH = "//*[@id='password']"

SUBMIT_BUTTON_XPATH = "//*[@id='submit']"

LOGIN_FORM_1_STEP = LoginForm1Step(
    username_input_xpath=USERNAME_INPUT_XPATH,
    password_input_xpath=PASSWORD_INPUT_XPATH,
    submit_button_xpath=SUBMIT_BUTTON_XPATH,
    url=internal_url.LOG_IN_1_STEP,
)

LOGIN_FORM_2_STEPS = LoginForm2Steps(
    username_input_xpath=USERNAME_INPUT_XPATH,
    username_submit_button_xpath=SUBMIT_BUTTON_XPATH,
    password_input_xpath=PASSWORD_INPUT_XPATH,
    password_submit_button_xpath=SUBMIT_BUTTON_XPATH,
    url=internal_url.LOG_IN_2_STEPS,
)
