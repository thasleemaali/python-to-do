import random
import math

while True:
    number = random.randint(1, 100)
    if math.isqrt(number) ** 2 == number:
        print(f"Perfect square found: {number}")
        print(f"Square root: {math.isqrt(number)}")
        break