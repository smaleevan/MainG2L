"""Utility modules for MainG2L."""

from .string_utils import (
    capitalize_words,
    truncate,
    is_palindrome,
    count_words,
    reverse_string,
)
from .math_utils import (
    factorial,
    is_prime,
    fibonacci,
    clamp,
    percentage,
)
from .file_utils import (
    read_lines,
    write_lines,
    file_exists,
    count_lines,
)

__all__ = [
    "capitalize_words",
    "truncate",
    "is_palindrome",
    "count_words",
    "reverse_string",
    "factorial",
    "is_prime",
    "fibonacci",
    "clamp",
    "percentage",
    "read_lines",
    "write_lines",
    "file_exists",
    "count_lines",
]
