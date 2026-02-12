from . import regex


def prompt_user_for_value(prompt_message: str, validate_input_regex: str | None) -> str:
    user_input = input(prompt_message)
    if validate_input_regex is not None:
        while regex.is_value_valid(user_input, validate_input_regex) is False:
            print(
                f"Invalid input. Please try again. The input format should follow this regex pattern: {validate_input_regex}"
            )
            user_input = input(prompt_message)
    return user_input
