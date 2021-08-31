"""Part 3 of ex01."""

__author__ = "730394836"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
left_int = int(left)
right_int = int(right)
less_than = left_int < right_int 
greater_equal = left_int >= right_int
equal = left_int == right_int
not_equal = left_int != right_int
print(left + " < " + right + " is " + str(less_than))
print(left + " >= " + right + " is " + str(greater_equal))
print(left + " == " + right + " is " + str(equal))
print(left + " != " + right + " is " + str(not_equal))