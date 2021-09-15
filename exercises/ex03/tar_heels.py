"""An exercise in remainders and boolean logic."""

__author__ = "730394836"


num: int = int(input("Enter an int: "))

if (num % 2) + (num % 7) == 0:
    print("TAR HEELS")
else:
    if (num % 2) == 0:
        print("TAR")
    else:
        if (num % 7) == 0:
            print("HEELS")
        else: 
            print("CAROLINA")