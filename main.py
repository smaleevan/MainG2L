"""Entry point demonstrating the MainG2L utility library."""

from utils import (
    capitalize_words,
    truncate,
    is_palindrome,
    count_words,
    reverse_string,
    factorial,
    is_prime,
    fibonacci,
    clamp,
    percentage,
)


def demo_string_utils() -> None:
    """Demonstrate string utility functions."""
    print("=== String Utilities ===")
    print(capitalize_words("the quick brown fox"))
    print(truncate("This is a long sentence that will be shortened.", 20))
    print(is_palindrome("A man a plan a canal Panama"))
    print(count_words("  Hello beautiful world  "))
    print(reverse_string("Python"))
    print()


def demo_math_utils() -> None:
    """Demonstrate math utility functions."""
    print("=== Math Utilities ===")
    print(f"5! = {factorial(5)}")
    print(f"is_prime(13) = {is_prime(13)}")
    print(f"fibonacci(8) = {fibonacci(8)}")
    print(f"clamp(150, 0, 100) = {clamp(150, 0, 100)}")
    print(f"percentage(1, 4) = {percentage(1, 4)}%")
    print()


def main() -> None:
    """Run all demonstrations."""
    demo_string_utils()
    demo_math_utils()


if __name__ == "__main__":
    main()
