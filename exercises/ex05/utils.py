"""List utility functions part 2."""

__author__ = "730394836"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the even numbers of a list."""
    i: int = 0
    evens: list[int] = []
    while i < len(nums):
        if (nums[i] % 2) == 0:
            evens.append(nums[i])
        else: 
            return evens
        i += 1
    return evens