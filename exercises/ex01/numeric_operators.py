"""Part 2 of ex01."""

__author__ = "730394836"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
left_int = int(left) 
right_int = int(right)
power_raise = left_int ** right_int
reg_div = left_int / right_int
int_div = left_int // right_int
remainder = left_int % right_int
print(left + " ** " + right + " is " + str(power_raise))
print(left + " / " + right + " is " + str(reg_div))
print(left + " // " + right + " is " + str(int_div))
print(left + " % " + right + " is " + str(remainder))