"""Tests for math utility functions."""

import pytest
from utils.math_utils import (
    factorial,
    is_prime,
    fibonacci,
    clamp,
    percentage,
)


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_small(self):
        assert factorial(5) == 120

    def test_larger(self):
        assert factorial(10) == 3628800

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)


class TestIsPrime:
    def test_zero_not_prime(self):
        assert is_prime(0) is False

    def test_one_not_prime(self):
        assert is_prime(1) is False

    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_three_is_prime(self):
        assert is_prime(3) is True

    def test_four_not_prime(self):
        assert is_prime(4) is False

    def test_large_prime(self):
        assert is_prime(97) is True

    def test_large_not_prime(self):
        assert is_prime(100) is False

    def test_negative_not_prime(self):
        assert is_prime(-7) is False


class TestFibonacci:
    def test_zero_terms(self):
        assert fibonacci(0) == []

    def test_one_term(self):
        assert fibonacci(1) == [0]

    def test_two_terms(self):
        assert fibonacci(2) == [0, 1]

    def test_six_terms(self):
        assert fibonacci(6) == [0, 1, 1, 2, 3, 5]

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            fibonacci(-1)


class TestClamp:
    def test_within_range(self):
        assert clamp(5, 0, 10) == 5

    def test_below_minimum(self):
        assert clamp(-5, 0, 10) == 0

    def test_above_maximum(self):
        assert clamp(15, 0, 10) == 10

    def test_at_minimum(self):
        assert clamp(0, 0, 10) == 0

    def test_at_maximum(self):
        assert clamp(10, 0, 10) == 10

    def test_float_values(self):
        assert clamp(0.5, 0.0, 1.0) == 0.5


class TestPercentage:
    def test_basic(self):
        assert percentage(25, 200) == 12.5

    def test_full_amount(self):
        assert percentage(100, 100) == 100.0

    def test_zero_part(self):
        assert percentage(0, 50) == 0.0

    def test_zero_total_raises(self):
        with pytest.raises(ValueError):
            percentage(10, 0)

    def test_float_inputs(self):
        assert percentage(1, 4) == 25.0
