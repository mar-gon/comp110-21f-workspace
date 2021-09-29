"""List utility functions."""

__author__ = "730394836"


# TODO: Implement your functions here.
def all(items: list[int], num: int) -> bool:
    """Indicates whether the given number is the same as all numbers in a list."""
    i: int = 0
    if len(items) == 0:
        return False 
    while i < len(items):
        while num != items[i]:
            return False
        i += 1
    return True


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Tests if two lists are the same."""
    i: int = 0
    while i < len(l1) and i < len(l2):
        while l1[i] != l2[i] or len(l1) != len(l2):
            return False
        i += 1
    return True


def max(items: list[int]) -> int:
    """Returns the largest number in a list."""
    i: int = 0
    if len(items) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(items):
        next_num: int = i + 1 
        while next_num < len(items):
            if items[i] >= items[next_num] and items[i] >= items[i - 1]:
                max_num = items[i]
            next_num += 1
        i += 1
    return max_num
