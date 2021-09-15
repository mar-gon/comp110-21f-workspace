"""Drawing forests in a loop."""

__author__ = "730394836"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
seeds: int = 1

while seeds <= depth:
    print(TREE * seeds)
    seeds += 1