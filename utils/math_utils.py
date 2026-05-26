"""Math utility functions."""

from typing import List


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer.

    Args:
        n: A non-negative integer.

    Returns:
        n! (n factorial).

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError(f"factorial() is not defined for negative numbers: {n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Check whether an integer is a prime number.

    Args:
        n: The integer to test.

    Returns:
        True if n is a prime number, False otherwise.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> List[int]:
    """Return the first n Fibonacci numbers.

    Args:
        n: How many Fibonacci numbers to generate.

    Returns:
        A list containing the first n Fibonacci numbers.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> fibonacci(6)
        [0, 1, 1, 2, 3, 5]
    """
    if n < 0:
        raise ValueError(f"fibonacci() requires a non-negative count, got {n}")
    if n == 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Clamp a value between a minimum and maximum.

    Args:
        value: The value to clamp.
        minimum: The lower bound.
        maximum: The upper bound.

    Returns:
        minimum if value < minimum, maximum if value > maximum, else value.

    Examples:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(5, 0, 10)
        5
    """
    return max(minimum, min(value, maximum))


def percentage(part: float, total: float) -> float:
    """Calculate what percentage part is of total.

    Args:
        part: The partial value.
        total: The total value.

    Returns:
        The percentage as a float between 0 and 100.

    Raises:
        ValueError: If total is zero.

    Examples:
        >>> percentage(25, 200)
        12.5
    """
    if total == 0:
        raise ValueError("total must not be zero")
    return (part / total) * 100
