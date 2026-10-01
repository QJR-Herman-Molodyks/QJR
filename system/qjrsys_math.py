import math

def give_abs(number):
    try:

        if number > int(number) and number>0:
            print(abs(number))
        elif number < int(number) and number<0:
            print(abs(number))
        else:
            print(abs(int(number)))

    except ValueError:
        print("\033[31mABS: Invalid input. Please enter a valid number.\033[0m")


def give_round(number):
    try:
        print(round(number))
    except ValueError:
        print("\033[31mROUND: Invalid input. Please enter a valid number.\033[0m")


def give_sqrt(number):
    try:
        if number < 0:
            print("\033[31mSQRT: Cannot compute square root of a negative number.\033[0m")
        else:
            print(number ** 0.5)
    except ValueError:
        print("\033[31mSQRT: Invalid input. Please enter a valid number.\033[0m")


def give_cos(number):
    try:
        print(math.cos(number))
    except ValueError:
        print("\033[31mCOS: Invalid input. Please enter a valid number.\033[0m")


def give_sin(number):
    try:
        print(math.sin(number))
    except ValueError:
        print("\033[31mSIN: Invalid input. Please enter a valid number.\033[0m")


def give_tan(number):
    try:
        print(math.tan(number))
    except ValueError:
        print("\033[31mTAN: Invalid input. Please enter a valid number.\033[0m")


def give_log(number):
    try:
        if number <= 0:
            print("\033[31mLOG: Cannot compute logarithm of non-positive numbers.\033[0m")
        else:
            print(math.log(number))
    except ValueError:
        print("\033[31mLOG: Invalid input. Please enter a valid number.\033[0m")

def give_exp(number):
    try:
        print(math.exp(number))
    except ValueError:
        print("\033[31mEXP: Invalid input. Please enter a valid number.\033[0m")


def give_factorial(number):
    try:
        print(math.factorial(number))
    except TypeError:
        print("\033[31mFACTORIAL: Invalid input. Please enter  valid number.\033[0m")

