"""An Illusory Choose Your Own Adventure Game."""

__author__ = "730394836"

points: int
player: str
BABY: str = "\U0001F476"
ANGRY_BABY: str = "\U0001F621"
BABY_LOVE: str = "\U00002764"


def greet() -> None:
    """Function greets player."""
    global player
    print("Welcome! You are about to enter a story driven experience.")
    print("You will be able to make choices and choose your own path, which may add or subtract points.")
    print("To make a choice, you will be prompted to enter a number or a word responce. Capitalization in words matter.")
    player = input("Are you ready? Lets begin! But first, what is your name? ")


def main() -> None:
    """The program's entrypoint."""
    greet()
    global points
    global player
    points = 0
    print("You are taking a stroll in the woods behind your house, as you usually do after a long day.")
    three_choices: int = int(input("You suddenly notice a strange hand-held game console on the ground. Do you... 1) Leave it, 2) Pick it up, or 3) Smash it? "))
    if three_choices == 1:
        print("You think it must belong to someone and that they will soon be back to look for it. You leave it there.") 
        print("You then realize the sun is beginning to set, so you head back home.") 
        print("You wonder what game is in the console...") 
    if three_choices == 2:
        print("You pick up the console and it immediately turns on. The screen reads:")
        print(f"HI {player}, THIS IS BABY {BABY}.")
        print("You wonder how it knows your name... but the next prompt interrupts your thought:")
        play_choice: str = input(f"DO YOU WANT TO PLAY WITH BABY{BABY}{BABY_LOVE} ? Enter YES or NO: ")
        if play_choice == "YES":
            points += 1
        if play_choice == "NO":
            points -= 2
            print(f"BABY IS ANGRY{ANGRY_BABY}. THAT WAS NOT NICE, {player}")
            print("You feel bad for Baby, or maybe you feel threatened... either way you decide to try again and play with Baby.")
            print(f"The screen now reads: BABY IS HAPPY! {BABY}{BABY_LOVE}")
    if three_choices == 3:
        smash_choice(points)


def smash_choice(p: int) -> int:
    global player
    """Enters choice 3 of inital choices and alters points."""
    print("You had a really bad day today. Instead of dealing with your emotions in a mature way, you decide to take it out on the console.")
    print("You grab a rock, but right before you are about to smash it, the console it turns on an reads:")
    print(f"NOW, NOW, {player}, I WOULDN'T DO THAT IF I WERE YOU. THIS IS BABY {BABY}. YOU SHOULDN'T HURT A BABY.")
    print(f"BE A GOOD ROLE MODEL AND APOLOGIZE{ANGRY_BABY}.")
    apology: str = input("You are very freaked out, so you apologize to Baby. Enter SORRY: ")
    if apology == "SORRY":
        p += 1
    return p


if __name__ == "__main__":
    main()