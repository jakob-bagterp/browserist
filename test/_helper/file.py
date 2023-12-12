def create(file_path: str) -> None:
    """Create test file."""

    with open(file_path, "w") as file:
        file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
