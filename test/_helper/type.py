from collections.abc import Callable
from pathlib import Path

from browserist.model.type.file_png import FilePNG
from browserist.model.type.ip import IPPort, IPv4
from browserist.model.type.path import FilePath
from browserist.model.type.url import URL
from browserist.model.type.xpath import XPath

FilePathCallable = Callable[[FilePath], FilePath]
FilePNGCallable = Callable[[FilePNG], FilePNG]
IPv4Callable = Callable[[IPv4], IPv4]
IPPortCallable = Callable[[IPPort], IPPort]
URLCallable = Callable[[URL], URL]
XPathCallable = Callable[[XPath], XPath]


def validate_repr(tiny_type: FilePNG | FilePath | IPv4 | URL | XPath, expected_output: str) -> None:
    """Test that the __repr__ dunder method of a tiny type represents itself as a string."""

    assert expected_output == repr(tiny_type)


def validate_representation(type: FilePNGCallable | IPv4Callable | URLCallable | XPathCallable, input: str) -> None:
    """Test that a tiny type represents itself as a string."""

    expected_output = input
    tiny_type = type(input)
    assert expected_output == tiny_type
    assert expected_output == tiny_type.value
    validate_repr(tiny_type, expected_output)


def validate_representation_file_path(type: FilePathCallable, input: str | Path) -> None:
    """Test that the FilePath tiny type represents itself as a string."""

    expected_output = input
    file_path = type(input)
    if isinstance(input, Path):
        assert expected_output == file_path.path
        assert str(expected_output.resolve()) == file_path == str(file_path.path.resolve())
    else:
        assert expected_output == file_path
        assert expected_output == str(file_path.path.resolve())
    expected_output_as_string = str(expected_output) if isinstance(expected_output, Path) else expected_output
    validate_repr(file_path, expected_output_as_string)


def validate_bypass(
        type: FilePathCallable | FilePNGCallable | IPv4Callable | IPPortCallable | URLCallable | XPathCallable,
        input: FilePath | Path | FilePNG | IPv4 | IPPort | URL | XPath | str | int
) -> None:
    """Test that if an input already is a validated tiny type element, bypass and don't create a new object."""

    tiny_type = type(input)
    assert tiny_type is type(tiny_type)
    assert type(input) is not type(input)
