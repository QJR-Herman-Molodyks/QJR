
from random import randint


def run_app():
    print("Please select a mode:    \n"
          "1). Select a range      \n"
          "2). Use a default range \n"
          "3). Exit a game.        \n")

    while True:
        choice = int(input("Choice> "))
        if choice == 1:
            print("Please select a range: ")
            num_from = int(input("From: "))
            num_to = int(input("To: "))

            get_random_number_from_range(num_from, num_to)

        elif choice == 2:
            get_random_number()

        elif choice == 3:
            break

        else:
            print("Option is not found!!!")

def get_random_number():
    random_num = randint(1, 100)

    while True:
        user_input = int(input("Enter a number: "))

        if user_input > random_num:
            print("Random number is less.")
        elif user_input < random_num:
            print("Random number is higher.")
        elif user_input == random_num:
            print("Yeah! You have guessed it!!!")
            break
        else:
            print("Error!!!")

def get_random_number_from_range(num1, num2):
    random_num2 = randint(num1, num2)

    while True:
        user_input = int(input("Enter a number: "))

        if user_input > random_num2:
            print("Random number is less.")
        elif user_input < random_num2:
            print("Random number is higher.")
        elif user_input == random_num2:
            print("Yeah! You have guessed it!!!")
            break
        else:
            print("Error!!!")

def run_and_debug():
    try:
        run_app()

    except ValueError:
        print("\033[31mEnter a number please (Not float, not text)\033[0m")

    except Exception as e:
        print(f"\033[31mERROR: {e}\033[0m")

if __name__ == "__main__":
    run_and_debug()

