REMOVE_BODY_ELEMENT = """
    var html = document.getElementsByTagName('html');
    var body = html[0];
    body.removeChild(document.body);
"""


def remove_element(xpath: str) -> str:
    return f"""
        var element = document.evaluate('{xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        element.remove();
        """
