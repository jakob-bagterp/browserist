from typing import Callable

from browserist.model.type.file_png import FilePNG
from browserist.model.type.url import URL
from browserist.model.type.xpath import XPath

FilePNGCallable = Callable[[FilePNG], FilePNG]
URLCallable = Callable[[URL], URL]
XPathCallable = Callable[[XPath], XPath]


def validate_representation(type: FilePNGCallable | URLCallable | XPathCallable, input: str) -> None:
    """Test that a tiny type represents itself as a string."""

    tiny_type_input = expected_output = input
    tiny_type = type(tiny_type_input)
    assert expected_output == tiny_type
    assert expected_output == tiny_type.value


def validate_bypass(type: FilePNGCallable | URLCallable | XPathCallable, input: str) -> None:
    """Test that if an input already is a validated tiny type element, bypass and don't create a new object."""

    tiny_type = type(input)
    assert tiny_type is type(tiny_type)
    assert type(input) is not type(input)
