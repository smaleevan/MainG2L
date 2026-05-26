"""String utility functions."""


def capitalize_words(text: str) -> str:
    """Return the text with each word capitalized.

    Args:
        text: The input string.

    Returns:
        The string with every word capitalized.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return text.title()


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to a maximum length, appending a suffix if shortened.

    Args:
        text: The input string.
        max_length: Maximum allowed length of the returned string (including suffix).
        suffix: String appended when truncation occurs. Defaults to '...'.

    Returns:
        The original string if it fits within max_length; otherwise a truncated
        version ending with suffix.

    Examples:
        >>> truncate("Hello, world!", 8)
        'Hello...'
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def is_palindrome(text: str) -> bool:
    """Check whether a string is a palindrome (ignores case and spaces).

    Args:
        text: The input string.

    Returns:
        True if the cleaned string reads the same forwards and backwards.

    Examples:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """Count the number of words in a string.

    Args:
        text: The input string.

    Returns:
        The number of whitespace-separated tokens.

    Examples:
        >>> count_words("  Hello world  ")
        2
    """
    return len(text.split())


def reverse_string(text: str) -> str:
    """Return the reverse of a string.

    Args:
        text: The input string.

    Returns:
        The string with characters in reverse order.

    Examples:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]
