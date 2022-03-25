from dataclasses import dataclass


@dataclass
class LoginCredentials:
    """Object to define a user profile's access credentials.

    Separated from the login form so that the multiple users/roles can use the same form."""

    username: str
    password: str
