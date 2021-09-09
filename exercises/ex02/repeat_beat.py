"""Repeating a beat in a loop."""

__author__ = "730394836"


beat: str = input("What beat do you want to repeat? ")
reps: int = int(input("How many times do you want to repeat it? "))
rep_beat = ((beat + " ") * (reps - 1) + beat)

while reps <= 0:
    print("No beat...")
    reps = (reps * -1) + 1
while reps > 0:
    print(rep_beat)
    reps = reps - reps
