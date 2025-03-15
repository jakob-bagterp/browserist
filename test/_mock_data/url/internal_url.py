from _helper import directory

from browserist.helper.directory import update_path_format_if_windows

_web_mock_data_directory = directory.get_path_for_web_mock_data()

CHECKBOXES: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/checkboxes.html")

COOKIE_BANNER_WITH_IFRAME: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/cookie_banner/page_with_iframe.html")

COOKIE_BANNER_WITHOUT_IFRAME: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/cookie_banner/page_without_iframe.html")

DOWNLOAD: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/download/page.html")

DROPDOWN_SELECTOR: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/drop-down_selector.html")

LOG_IN_1_STEP: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/log_in/1_step/login_form.html")

LOG_IN_2_STEPS: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/log_in/2_steps/1_username/login_form.html")

MINI_SITE_DIR: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/mini_site")

MINI_SITE_ABOUT: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/about.html")

MINI_SITE_CONTACT: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/contact.html")

MINI_SITE_FEATURE_1: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/feature_1.html")

MINI_SITE_FEATURE_2: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/feature_2.html")

MINI_SITE_FEATURE_3: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/feature_3.html")

MINI_SITE_HOMEPAGE: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/homepage.html")

MINI_SITE_ASSETS_DIR: str = update_path_format_if_windows(
    f"{MINI_SITE_DIR}/assets")

MINI_SITE_IMAGE_LAB_MICROSCOPE: str = update_path_format_if_windows(
    f"{MINI_SITE_ASSETS_DIR}/pexels-chokniti-khongchum-1197604-2280547_medium.jpg")

MINI_SITE_IMAGE_LAB_TEST_TUBES: str = update_path_format_if_windows(
    f"{MINI_SITE_ASSETS_DIR}/pexels-chokniti-khongchum-1197604-2280549_medium.jpg")

MINI_SITE_IMAGE_LAB_PETRI_DISH: str = update_path_format_if_windows(
    f"{MINI_SITE_ASSETS_DIR}/pexels-chokniti-khongchum-1197604-2280568_medium.jpg")

MINI_SITE_IMAGE_LAB_SAMPLES: str = update_path_format_if_windows(
    f"{MINI_SITE_ASSETS_DIR}/pexels-chokniti-khongchum-1197604-2280571_medium.jpg")

MINI_SITE_IMAGE_OFFICE_IDEAS_ON_BOARD: str = update_path_format_if_windows(
    f"{MINI_SITE_ASSETS_DIR}/pexels-startup-stock-photos-212286_medium.jpg")

NO_BODY: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/no_body.html")

NOT_SCROLLABLE: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/scroll/not_scrollable.html")

RADIO_BUTTONS: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/radio_buttons.html")

SEARCH: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/search/search_form.html")

SCROLL_CANVAS: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/scroll/canvas/page.html")

SCROLL_LONG_VERTICAL: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/scroll/long_vertical/page.html")

SCROLL_WIDE_HORIZONTAL: str = update_path_format_if_windows(
    f"file://{_web_mock_data_directory}/scroll/wide_horizontal/page.html")
