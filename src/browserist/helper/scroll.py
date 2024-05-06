def is_valid_page_number(page_number: int) -> bool:
    return isinstance(page_number, int) and page_number >= 1
