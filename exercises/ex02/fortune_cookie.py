"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394836"


from random import randint

print("Your fortune cookie says...")
fortune: int = randint(1, 4)

if fortune == 1:
    print("A small handsome toad will visit you soon.")
else:
    if fortune == 2:
        print("You will be blessed by Kris Jordan with advanced programming skills.")
    else: 
        if fortune == 3:
            print("The Covid-19 pandemic will soon come to an end.")
        else:
            if fortune == 4:
                print("You will grow an inch taller!")
print("Now, go spread positive vibes!")