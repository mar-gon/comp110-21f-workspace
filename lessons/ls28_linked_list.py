"""Simple linked list example."""
from __future__ import annotations
from typing import Optional


class Node:
    """Single linked list Node."""
    data: int 
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor."""
        self.data = data
        self.next = next


second_node: Node = Node(2, None)
a_node: Node = Node(1, second_node)
