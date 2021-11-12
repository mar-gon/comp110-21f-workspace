"""Examples of optional parameters and Union types."""
from typing import Union



def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    if isinstance(name, int):
        greeting += "COMP" + str(name)
    return greeting


print(hello("Sally"))

# No parameter
print(hello())

# int works too!
print(hello(110))