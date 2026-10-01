
from random import randint

def randomize():
    a = int(input("The first number: "))
    b = int(input("The second number: "))
    print(f"Randomized: {randint(a, b)}")
