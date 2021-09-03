"""Example of a while-loop statement."""

counter: int = 0
maximum: int = int(input("What number do you want to count up to? "))

while counter <= maximum: 
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("done!")
