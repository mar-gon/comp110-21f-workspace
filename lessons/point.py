"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x & y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates multiple components by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Method that doesnt mutate the Point."""
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)
        return scaled_point


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
print(f"{p0.x}, {p0.y}")
p1: Point = p0.scale(2.0)
print(f"{p1.x}, {p1.y}")