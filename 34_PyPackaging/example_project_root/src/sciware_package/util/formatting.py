def canonicalize_string(base_string: str) -> str:
    """Convert a base string into a canonical representation for our application.

    Args:
        base_string (str): The input string to canonicalize.

    Returns:
        str: An explicit "empty string" representation, if an empty
        string was originally passed; otherwise, the input string,
        with the first character capitalized and the rest in lower case.
    """
    if (base_string == ''):
        return "[empty string]"
    return base_string.capitalize()
