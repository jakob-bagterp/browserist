class LoginException(Exception):
    def __init__(self, username: str) -> None:
        self.message = f"Something went wrong when trying to log in with username \"{username}\". Please try again..."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
