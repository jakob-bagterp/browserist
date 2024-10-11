def strip_whitespace(html: str) -> str:
    """Strip whitespace from HTML.

    Args:
        html (str): HTML source.

    Returns:
        HTML source without whitespace.
    """

    return html.replace("\n", "").replace("\t", "").replace("  ", "")
