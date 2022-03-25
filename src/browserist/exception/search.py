class SearchException(Exception):
    def __init__(self, term: str) -> None:
        self.message = f"Something went wrong when trying to search for \"{term}\". Please try again..."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
