#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
reminder = number % 10
if number < 0:
    reminder = -reminder
output = ''
if reminder == 0:
    output = "0"
elif reminder > 5:
    output = "greater than 5"
else:
    output = "less than 6 and not 0"
print(f"Last digit of {number} is {reminder} and is {output}")
