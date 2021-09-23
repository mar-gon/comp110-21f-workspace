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
    game_loop: int = 0
    while game_loop >= 0:
        print("You are taking a stroll in the woods behind your house, as you usually do after a long day.")
        three_choices: int = int(input("You suddenly notice a strange hand-held game console on the ground. Do you... 1) Leave it, 2) Pick it up, or 3) Smash it? "))
        if three_choices == 1:
            print("You think it must belong to someone and that they will soon be back to look for it. You leave it there.") 
            print("You then realize the sun is beginning to set, so you head back home.") 
            print("You wonder what game is in the console... you hope the owner doesnt find it, so that you can check it out again tomorrow.") 
        if three_choices == 2:
            print("You pick up the console and it immediately turns on. The screen reads:")
            print(f"HI {player}, THIS IS BABY {BABY}.")
            print("You wonder how it knows your name... but the next prompt interrupts your thought:")
            play_choice: str = input(f"DO YOU WANT TO PLAY WITH BABY{BABY}{BABY_LOVE} ? Enter YES or NO: ")
            if play_choice == "YES":
                points += 5
                print("You play with baby for awhile.")
            if play_choice == "NO":
                points -= 1
                print(f"BABY IS ANGRY{ANGRY_BABY}. THAT WAS NOT NICE, {player}")
                print("You feel bad for Baby, or maybe you feel threatened... either way you decide to try again and play with Baby.")
                print(f"The screen now reads: BABY IS HAPPY! {BABY}{BABY_LOVE}")
            leaving_baby()
        if three_choices == 3:
            points += smash_choice(points)
            print("The screen then prompts you to play with Baby. You do as you're told to avoid further conflict.")
            leaving_baby()
        end_choice: int = int(input("You have reached an ending. Would you like to 1) Quit game, or 2) Go back to finding the console? "))
        if end_choice == 1:
            game_loop = game_loop - 1
            print("GAME OVER.")
        print(f"Points accumulated: {points}")
        

def smash_choice(p: int) -> int:
    """Enters choice 3 of inital choices and alters points."""
    global player
    print("You had a really bad day today. Instead of dealing with your emotions in a mature way, you decide to take it out on the console.")
    print("You grab a rock, but right before you are about to smash it, the console it turns on an reads:")
    print(f"NOW, NOW, {player}, I WOULDN'T DO THAT IF I WERE YOU. THIS IS BABY {BABY}. YOU SHOULDN'T HURT A BABY.")
    print(f"BE A GOOD ROLE MODEL AND APOLOGIZE{ANGRY_BABY}.")
    apology: str = input("You are very freaked out, so you apologize to Baby. Enter SORRY: ")
    if apology == "SORRY":
        p += 1
    return p


def leaving_baby() -> None:
    """Advances the game's story line."""
    global points
    global player
    leaving_choice: str = input("You then realize it is getting late and think about going home. Do you want to keep playing with baby? Enter YES or NO: ")
    if leaving_choice == "YES":
        points += 5
        print(f"The screen flashes: BABY IS HAPPY YOU STAYED{BABY}{BABY_LOVE}. BABY CAN SENSE ABANDONMENT. YOU MUST NEVER STOP PLAYING WITH BABY.")
        print("IF YOU LEAVE BABY, BABY WILL EXPOSE ALL YOUR SECRETS TO THE INTERNET.")
        print("You doubt Baby knows any of your secrets. But then again... how did Baby know your name?")
        print(f"The screen flashes again: BABY KNOWS EVERYTHING ABOUT YOU, {player}. BABY ALSO KNOWS WHAT YOU'RE THINKING.")
        print("IN FACT, BABY CREATED YOU. BABY IS YOUR GOD. EVERYTHING IN YOUR LIFE HAS LED UP TO FINDNG BABY. YOU HAVE ALWAYS BEEN UNDER BABY'S CONTROL.")
        print(f"YOU WILL PLAY WITH BABY FOREVER{BABY}{BABY_LOVE}.")
    else:
        while leaving_choice == "NO":
            points -= 1
            from random import randint
            threat: int = randint(1, 6)
            if threat == 1:
                print(f"The screen flashes: IT'S NOT A WISE CHOICE TO STOP PLAYING WITH BABY{ANGRY_BABY}, {player}.")
            if threat == 2:
                print(f"The screen flashes: IF YOU LEAVE BABY, BABY WILL EXPOSE ALL YOUR SECRETS TO THE INTERNET{BABY}{BABY_LOVE}.")
            if threat == 3:
                print("The screen flashes: YOU MUST KEEP PLAYING WITH BABY, OR ELSE BABY WILL DOXX YOU TO THE DARK WEB.")
            if threat == 4:
                print(f"The screen flashes: ARE YOU SURE ABOUT THAT? BABY CAN, AND WILL, RUIN YOUR LIFE{BABY}{BABY_LOVE}.")
            if threat == 5:
                print("The screen flashes: IF YOU STOP PLAYING WITH BABY, BABY WILL POST THOSE EMBARRASSING PICTURES OF YOU FROM HIGHSCHOOL.")
            if threat == 6:
                print("The screen flashes: BABY KNOWS WHAT YOU DID LAST SUMMER. THINK TWICE ABOUT LEAVING BABY.")
            leaving_choice = input("Do you want to keep playing with baby? Enter YES or NO: ")
        print(f"The screen now reads: SEE, {player}, WAS IT SO HARD TO JUST SAY YES?")
        print("YOU CAN NEVER DENY THE WILL OF BABY. YOU HAVE NO CHOICE.")
        print(f"YOU SEE, {player}, BABY CREATED YOU. BABY IS YOUR GOD. EVERYTHING IN YOUR LIFE HAS LED UP TO FINDNG BABY. YOU HAVE ALWAYS BEEN UNDER BABY'S CONTROL.")
        print(f"YOU WILL PLAY WITH BABY FOREVER{BABY}{BABY_LOVE}.")


if __name__ == "__main__":
    main()