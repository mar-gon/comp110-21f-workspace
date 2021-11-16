"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730394836"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, num: float, rep: int) -> None:
        """Altering Simpy's values."""
        self.values = []
        i: int = 0
        while i < rep:
            self.values.append(num)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fills in a range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        if step < 0.0:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Returns the sum of all values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.values.append(value + rhs)
        return result
 
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for raising power."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        if isinstance(rhs, Simpy): 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result