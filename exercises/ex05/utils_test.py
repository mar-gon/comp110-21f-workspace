"""Unit tests for list utility functions."""

# in terminal: python -m pytest exercises/ex05
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730394836"

from exercises.ex05.utils import only_evens


def test_only_evens1() -> None:
    """Tests if it returns evens."""
    lis: list[int] = [1, 2, 3, 4]
    i: int = 0
    while i < len(only_evens(lis)):
        assert (only_evens(lis)[i] % 2) == 0
        i += 1


def test_only_evens2() -> None:
    """Tests if it returns blank if all odds."""
    lis: list[int] = [1, 3, 5]
    assert only_evens(lis) == []


def test_only_evens3() -> None:
    """Tests an empty list."""
    lis: list[int] = []
    assert only_evens(lis) == []