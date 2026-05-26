"""File utility functions."""

import os
from typing import List


def read_lines(filepath: str) -> List[str]:
    """Read all lines from a text file.

    Args:
        filepath: Path to the file.

    Returns:
        A list of lines with trailing newlines stripped.

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> lines = read_lines("example.txt")
    """
    with open(filepath, "r", encoding="utf-8") as fh:
        return [line.rstrip("\n") for line in fh]


def write_lines(filepath: str, lines: List[str]) -> None:
    """Write a list of lines to a text file, overwriting any existing content.

    Args:
        filepath: Path to the destination file.
        lines: Lines to write (newlines are added automatically).

    Examples:
        >>> write_lines("output.txt", ["Hello", "World"])
    """
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def file_exists(filepath: str) -> bool:
    """Check whether a file exists at the given path.

    Args:
        filepath: Path to check.

    Returns:
        True if a file exists at filepath, False otherwise.

    Examples:
        >>> file_exists("missing.txt")
        False
    """
    return os.path.isfile(filepath)


def count_lines(filepath: str) -> int:
    """Count the number of lines in a text file.

    Args:
        filepath: Path to the file.

    Returns:
        The number of lines in the file.

    Raises:
        FileNotFoundError: If the file does not exist.

    Examples:
        >>> count_lines("example.txt")
        3
    """
    with open(filepath, "r", encoding="utf-8") as fh:
        return sum(1 for _ in fh)
