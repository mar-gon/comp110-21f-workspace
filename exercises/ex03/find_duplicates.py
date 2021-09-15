"""Finding duplicate letters in a word."""

__author__ = "730394836"


word: str = input("Enter a word: ")
i: int = 0
dupe: int = 0

while i < len(word):
    letter: int = i + 1
    while letter < len(word):
        if word[letter] == word[i]:
            dupe = dupe + 1
        letter += 1
    i += 1
if dupe >= 1:
    print("Found duplicate: " + f"{dupe >= 1}")
else: 
    print("Found duplicate: " + f"{dupe >= 1}")