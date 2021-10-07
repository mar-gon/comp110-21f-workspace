"""List utility functions part 2."""

__author__ = "730394836"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the even numbers of a list."""
    i: int = 0
    evens: list[int] = []
    while i < len(nums):
        if (nums[i] % 2) == 0:
            evens.append(nums[i])
        i += 1
    return evens


def sub(original: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns list with items between start index and end index - 1."""
    new: list[int] = []
    i: int = 0
    if len(original) == 0:
        return new
    if start_index > len(original):
        return new
    if end_index <= 0:
        return new
    if start_index < 0:
        while i < end_index:
            new.append(original[i])
            i += 1
        return new
    if end_index < len(original):
        while start_index < end_index:
            new.append(original[start_index])
            start_index += 1 
    if end_index > len(original):
        while start_index < len(original):
            new.append(original[start_index])
            start_index += 1 
    return new


def concat(first: list[int], second: list[int]) -> list[int]:
    """Returns a list with the items of the first parameter list followed by the second's items."""
    both: list[int] = []
    i: int = 0 
    while i < len(first):
        both.append(first[i])
        i += 1
    i = 0
    while i < len(second):
        both.append(second[i])
        i += 1
    return both