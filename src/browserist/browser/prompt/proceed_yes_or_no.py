def prompt_proceed_yes_or_no() -> bool:
    # Input returns (note that pressing "Enter", i.e. an empty "", is considered "Yes"):
    YES_OPTIONS = {"yes", "y", ""}
    NO_OPTIONS = {"no", "n"}
    valid_choice = False  # Offset choice validation before while loop.

    while valid_choice is False:
        choice = input("Do you want to proceed (Y/N)? ").lower()
        if choice in YES_OPTIONS:
            valid_choice = True
            return True
        elif choice in NO_OPTIONS:
            valid_choice = True
            return False
        else:
            print("Please respond with \"Y\" or \"N\". Try again...")
    return False
