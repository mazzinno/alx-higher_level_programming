#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = abs(number) % 10
if number < 0:
    number2 = -number2
if number2 > 5:
    print(f"Last digit of {number} is {number2} and is greater than 5")
elif number2 % 10 == 0:
    print(f"Last digit of {number} is {number2} and is 0")
else:
    print(f"Last digit of {number} is {number2} and is less than 6 and not 0")
