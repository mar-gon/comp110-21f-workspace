"""Challenge question #1."""
__author__ = "730394836" 

choice: int = int(input("Enter a number: "))
# print A if choice < 25
# print B if choice >= 25
# print C if choice > 75
# print D if choice >= 50 and <= 75
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("D")
        else:
            print("C")