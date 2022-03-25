class CookieBannerException(Exception):
    def __init__(self) -> None:
        self.message = "Something went wrong when trying to accept cookies. Please try again..."
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
