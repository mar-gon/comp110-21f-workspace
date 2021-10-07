"""Unit tests for list utility functions."""

# in terminal: python -m pytest exercises/ex05

__author__ = "730394836"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


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


def test_sub1() -> None:
    """Tests if it returns subset list of items between start index & end index - 1."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub2() -> None:
    """Tests if it includes num @ end index if its greater than the len of original list."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 5) == [20, 30, 40]


def test_sub3() -> None:
    """Tests if when lenth of original list is zero, sub returns an empty list."""
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


def test_concat1() -> None:
    """Tests if it returns list including first list items followed by second list items."""
    first: list[int] = [1, 2, 3]
    second: list[int] = [4, 5, 6]
    assert concat(first, second) == [1, 2, 3, 4, 5, 6]


def test_concat2() -> None:
    """Tests if it returns empty list when both argument lists are empty."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat3() -> None:
    """Tests if it returns only second argument if first argument is empty."""
    first: list[int] = []
    second: list[int] = [1, 2, 3]
    assert concat(first, second) == [1, 2, 3]