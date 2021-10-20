"""Unit tests for dictionary functions."""

# python -m pytest exercises/ex06

__author__ = "123456789"

from exercises.ex06.dictionaries import invert
from exercises.ex06.dictionaries import favorite_colors
from exercises.ex06.dictionaries import count


def test_invert1() -> None:
    """Tests if it works with an empty value."""
    dic: dict[str, str] = {"a": ""}
    assert invert(dic) == {"": "a"}


def test_invert2() -> None:
    """Tests dictionary with one key."""
    dic: dict[str, str] = {"a": "x"}
    assert invert(dic) == {"x": "a"}


def test_invert3() -> None:
    """Tests dictionary with multiple keys."""
    dic: dict[str, str] = {"a": "x", "b": "y", "c": "z"}
    assert invert(dic) == {"x": "a", "y": "b", "z": "c"}


def test_favorite_colors1() -> None:
    """Tests if function works normally."""
    dic: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Mariana": "pink"}
    assert favorite_colors(dic) == "blue"


def test_favorite_colors2() -> None:
    """Tests if it returns 'no favorite colors' if no colors are repeated."""
    dic: dict[str, str] = {"Marc": "yellow", "Ezri": "green", "Kris": "blue", "Mariana": "pink", "Joe": "purple", "Lizzie": "red", "Pou": "orange"}
    assert favorite_colors(dic) == "No favorite colors."


def test_favorite_colors3() -> None:
    """Tests if it returns 'no favorite colors' if empty dict in argument."""
    dic: dict[str, str] = {}
    assert favorite_colors(dic) == "No favorite colors."


def test_count1() -> None:
    """Tests if function works normal."""
    items: list[str] = ["apple", "carrot", "tomato", "carrot", "apple"]
    assert count(items) == {"apple": 2, "carrot": 2, "tomato": 1}


def test_count2() -> None:
    """Tests when list only has one item."""
    items: list[str] = ["apple"]
    assert count(items) == {"apple": 1}


def test_count3() -> None:
    """Tests when given an empty list returns empty."""
    items: list[str] = []
    assert count(items) == {}
