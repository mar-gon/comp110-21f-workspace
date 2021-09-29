"""Example of for in syntax."""

names: list[str] = ["Mariana", "Kris", "Kaki", "Shrek"]

# example of using while loop
print("This is the while loop:")
i: int = 0 
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# example of for in loop
print("This is the for-in loop:")
for name in names:
    print(name)
# note that you dont have to define the variable outside of the for in func
