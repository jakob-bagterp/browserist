from copy import deepcopy

from _mock_data.url import internal_url

from browserist import LoginCredentials, LoginForm1Step, LoginForm2Steps

VALID_USERNAME = "johndoe"

VALID_PASSWORD = "password123"

INVALID = "invalid"

LOGIN_CREDENTIALS_VALID = LoginCredentials(username=VALID_USERNAME, password=VALID_PASSWORD)

LOGIN_CREDENTIALS_INVALID = LoginCredentials(username=INVALID, password=INVALID)

LOGIN_CREDENTIALS_INVALID_USERNAME = LoginCredentials(username=INVALID, password=VALID_PASSWORD)

LOGIN_CREDENTIALS_INVALID_PASSWORD = LoginCredentials(username=VALID_USERNAME, password=INVALID)

USERNAME_INPUT_XPATH = "//*[@id='username']"

PASSWORD_INPUT_XPATH = "//*[@id='password']"

SUBMIT_BUTTON_XPATH = "//*[@id='submit']"

SUCCESS_LANDING_PAGE = "homepage.html"

ERROR_LANDING_PAGE = "error.html"

LANDING_PAGE_HEADLINE_XPATH = "/html/body/h1"

LOGIN_FORM_1_STEP = LoginForm1Step(
    url=internal_url.LOG_IN_1_STEP,
    username_input_xpath=USERNAME_INPUT_XPATH,
    password_input_xpath=PASSWORD_INPUT_XPATH,
    submit_button_xpath=SUBMIT_BUTTON_XPATH,
    post_login_url_contains=SUCCESS_LANDING_PAGE,  # Eventually re-assign before test.
    post_login_element_xpath=LANDING_PAGE_HEADLINE_XPATH,
)

LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES = deepcopy(LOGIN_FORM_1_STEP)
LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES.return_bool = True

LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_URL = deepcopy(
    LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES
)
LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_URL.post_login_element_xpath = None

LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT = deepcopy(
    LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES
)
LOGIN_FORM_1_STEP_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT.post_login_url_contains = None

LOGIN_FORM_2_STEPS = LoginForm2Steps(
    url=internal_url.LOG_IN_2_STEPS,
    username_input_xpath=USERNAME_INPUT_XPATH,
    username_submit_button_xpath=SUBMIT_BUTTON_XPATH,
    password_input_xpath=PASSWORD_INPUT_XPATH,
    password_submit_button_xpath=SUBMIT_BUTTON_XPATH,
    post_login_url_contains=SUCCESS_LANDING_PAGE,  # Eventually re-assign before test.
    post_login_element_xpath=LANDING_PAGE_HEADLINE_XPATH,
)

LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES = deepcopy(LOGIN_FORM_2_STEPS)
LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES.return_bool = True

LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_URL = deepcopy(
    LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES
)
LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_URL.post_login_element_xpath = None

LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT = deepcopy(
    LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_BOTH_POST_LOGIN_ATTRIBUTES
)
LOGIN_FORM_2_STEPS_WITH_RETURN_BOOL_AND_POST_LOGIN_ELEMENT.post_login_url_contains = None
