"""An Illusory Choose Your Own Adventure Game."""

__author__ = "730394836"

points: int
player: str = input("what is your name? ")
BABY: str = "\U0001F476"
ANGRY_BABY: str = "\U0001F621"
BABY_LOVE: str = "\U00002764"


def main() -> None:
    """The program's entrypoint."""
    greet()
    # initialize global points in here
    # create game loop here


def greet() -> None:
    """Function greets player."""
    print("Welcome! You are about to enter a story driven experience.")
    print("You will be able to make choices and choose your own path.")
    print(f"Lets begin, but first, {player}")


if __name__ == "__main__":
    main()