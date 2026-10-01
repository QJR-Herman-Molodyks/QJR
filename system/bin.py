
def run_bit():
    version = "v1.5.2"
    bits = 8
    bit_storage = [0, 0, 0, 0, 0, 0, 0, 0]

    def bit_8():
        while True:
            user_input = input("\033[94mEnter a number (0-255): \033[0m")
            if user_input == "exit":
                break
            else:
                try:
                    number = int(user_input)
                    if 0 <= number < 2**bits:
                        for i in range(bits):
                            bit_storage[bits - 1 - i] = (number >> i) & 1
                        print("Binary representation:", ''.join(map(str, bit_storage)))
                    else:
                        print("Please enter a number between 0 and 255.")

                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                except Exception as e:
                    print("An error occurred:", e)

    print(f"Welcome to bin {version}! Enter 'exit' to quit.")
    print("Select a mode:              \n"
          "[1] Convert to bin (64-bit) \n"
          "[2] Convert to bin (8-bit)  \n"
          "[3] Exit                    \n"
          "                            \n")

    while True:
        try:
            choice = input("Mode> ")

            if choice == "exit":
                break
            elif choice == "":
                continue
            else:

                choice_int = int(choice)

                if choice_int == 1:
                    while True:
                        print("Convert to bin (64-Bit), enter 'exit' to exit. ")
                        binary = input("Enter a number to convert: ")

                        if binary == "exit":
                            break
                        else:
                            try:
                                bin_int = int(binary)
                                print(f" > {bin(bin_int)}")
                            except ValueError:
                                print("Enter a NUMBER!!!")
                            except Exception as e:
                                print(f"Error: {e}")

                elif choice_int == 2:
                    bit_8()

                elif choice_int == 3:
                    break

                else:
                    print("Error! Option is not found!!!")


        except ValueError:
            print("Enter a number!!!")
        except Exception as e:
            print(f"Error: {e}")




