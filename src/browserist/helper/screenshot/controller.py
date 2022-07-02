from .__init__ import default_file_name


def file_name(file_name: str | None) -> str:
    return default_file_name() if file_name is None else file_name
