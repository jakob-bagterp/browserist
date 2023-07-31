from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class LoginCredentials:
    """Object to define a user profile's access credentials.

    Note:
        Separated from the login form so that the multiple users/roles can use the same form.

    Args:
        username (str): Username, e.g. email.
        password (str): Password.
    """

    username: str
    password: str
