from ..... import helper
from .....constant import timeout
from ....get.page_title import get_page_title


def wait_until_page_title_changes(driver: object, baseline_text: str, timeout: int = timeout.DEFAULT) -> None:
    def has_page_title_changed(driver: object, baseline_text: str) -> bool:
        return get_page_title(driver) != baseline_text

    helper.retry.until_condition_is_true(driver, baseline_text, func=has_page_title_changed, timeout=timeout)
