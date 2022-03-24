import keyring
from _helper import external_url

from browserist import LoginCredentials, LoginForm1Step, LoginForm2Steps

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

JYLLANDSPOSTEN_LOGIN_CREDENTIALS = LoginCredentials(
    username=keyring.get_password("browserist-test-jyllandsposten-username", "username"),
    password=keyring.get_password("browserist-test-jyllandsposten-password", "password"),
)

JYLLANDSPOSTEN_LOGIN_FORM = LoginForm1Step(
    username_input_xpath="//*[@id='Username']",
    password_input_xpath="//*[@id='Password']",
    submit_button_xpath="//form//button[@type='submit']",
    url="https://medielogin.dk/Jyllands-posten/login?redirect=%2Fopenid%2Fendpoint%3Fopenid.claimed_id%3Dhttp%3A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.identity%3Dhttp%3A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.mode%3Dcheckid_setup%26openid.ns%3Dhttp%3A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.realm%3Dhttps%3A%252F%252Fauth.medielogin.dk%26openid.return_to%3Dhttps%3A%252F%252Fauth.medielogin.dk%252Fsignin-medielogin%253Fstate%253DoLr9PN4mpbzx-vdMxRFd6l8CAACXO-zn7kwowFdnh_96r7pw0_NvM4sBJiOnFzufIGaATmovvGi9yO9K6x2eBlpHyHDcwhBm9VEeqxOCdKDiN9wD3g7HC0jnQl_7fN35zaISQzwErT2gi3C3gdg-UeGbCsdXLbhv8u7AbKp8UoLDtefIv2PTSiGnM1-JpqmMj5q3OBj0IrxNtzT7G3Yyt4UUSccD1jSau7O7zncjRvPN6aVpxA4L8P5A8EIUY1YRrDbeMmBqwP9dQCwuW_w2bFMVEPMuj4vG6w633mGz1-fvzu-8qc5Vl_xfuTEO8PPLPnYfWQ5oyBlWJmEpRRWsxr94OQ1o2zPhDVK8aUeoD-HtfC3fcKG_v6QnLxrxOBNP_iTDkg0adA4o93cGL79-iJ6sQ0kS7dMiM_0uewD0HtOjp0qeh3tn4SiTcJGF06yVRMkhAgHEBRPCkKeo6-Ws9bg5OUAZ6YNkNiJf4U2rVlfiIapZFuarfGtd_q9-A5yxglTDOH3UyhI0tYZ4eaDInygLLarcsmNHpT8_wCPH29Q7hO63SCqD6XHVRkmGXisKl5JLc4OOWXiSuLPjOscpe-tUtsPkFFrZB6MyqpMv9WTFDud7dvFHOjy-iI5VNRIuJRw_u7XUNMBWnKN8fdZ6C3qj_hTr4OPQERkJ9WDCadmqAYIGnasTrUD5ZkhwwrBpkII-lts4_UjfIFfVeoFlSKF7kDFSPOKreX420Vkeoqv-CexTune4bNasswiBqC6MUGaFBdtt6xnqYWy3sgrNerZs3MtUQHbD1OtltkPTv9Qrys66IPFXoHUVrylO_yQmFTQicg%26openid.ns.mli%3Dhttp%3A%2F%2Fopenid.net%2Fsrv%2Fax%2F1.0%26openid.mli.brand%3DJyllands-posten",
    post_login_url=external_url.JYLLANDSPOSTEN_DK,
)
