#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digitofinal = number%10 - 10
else:
    digitofinal = number % 10
if digitofinal > 5:
    print(f'Last digit of {number} is {digitofinal} and is greater than 5')
elif digitofinal < 6 and digitofinal != 0:
    print(
        f'Last digit of {number} is {digitofinal} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {digitofinal} and is 0')
