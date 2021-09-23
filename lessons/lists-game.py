"""Example of using lists in a game."""

from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))
print(rolls)

# removing items on a list
rolls.pop(len(rolls) - 1)
print(rolls)

# summing values of a list
i: int = 0
sum: int = 0 
while i < len(rolls):
    sum = sum + rolls[i]
    i += 1
print(f"Total score: {sum}")

# adding items to the end of a list
# rolls.append(1)

# # how you can access an individual item in a list
# print(rolls[0])

# # finding number of items or length of a list
# print(len(rolls))

# # Accessing the last item of a list
# print(rolls[len(rolls) - 1])
