"""Example of a function that processes a list."""

# define a function named contains
# we can give two arguments: a needle value we're searching for in a haystack list


def main() -> None:
    names: list[str] = ["Kris", "Kaki", "Kris"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Returns True if neelde is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False


# python idiom for starting the main function
if __name__ == "__main__":
    main()
