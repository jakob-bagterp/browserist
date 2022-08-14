REMOVE_BODY_ELEMENT = """
    var html = document.getElementsByTagName('html');
    var body = html[0];
    body.removeChild(document.body);
"""
