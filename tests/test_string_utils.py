"""Tests for string utility functions."""

import pytest
from utils.string_utils import (
    capitalize_words,
    truncate,
    is_palindrome,
    count_words,
    reverse_string,
)


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_empty_string(self):
        assert capitalize_words("") == ""

    def test_single_word(self):
        assert capitalize_words("python") == "Python"

    def test_mixed_case(self):
        assert capitalize_words("hElLo WoRLd") == "Hello World"


class TestTruncate:
    def test_no_truncation_needed(self):
        assert truncate("Hi", 10) == "Hi"

    def test_exact_length(self):
        assert truncate("Hello", 5) == "Hello"

    def test_truncation_default_suffix(self):
        assert truncate("Hello, world!", 8) == "Hello..."

    def test_truncation_custom_suffix(self):
        assert truncate("Hello, world!", 7, "–") == "Hello,–"

    def test_empty_string(self):
        assert truncate("", 5) == ""

    def test_suffix_longer_than_max(self):
        # When max_length equals suffix length, result is just the suffix
        assert truncate("Hi there", 3) == "..."


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_single_character(self):
        assert is_palindrome("a") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_mixed_case(self):
        assert is_palindrome("Racecar") is True


class TestCountWords:
    def test_basic(self):
        assert count_words("hello world") == 2

    def test_leading_trailing_spaces(self):
        assert count_words("  hello world  ") == 2

    def test_empty_string(self):
        assert count_words("") == 0

    def test_single_word(self):
        assert count_words("python") == 1

    def test_multiple_spaces_between(self):
        assert count_words("a   b   c") == 3


class TestReverseString:
    def test_basic(self):
        assert reverse_string("hello") == "olleh"

    def test_empty_string(self):
        assert reverse_string("") == ""

    def test_single_character(self):
        assert reverse_string("a") == "a"

    def test_palindrome_unchanged(self):
        assert reverse_string("racecar") == "racecar"

    def test_numbers(self):
        assert reverse_string("12345") == "54321"
