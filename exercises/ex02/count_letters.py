"""Counting letters in a string."""

__author__ = "730394836"

letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i: int = 0
letter_count: int = 0

while i < len(word):
    if letter == word[i]:
        letter_count = letter_count + 1
    i = i + 1  
print("count: " + str(letter_count))
