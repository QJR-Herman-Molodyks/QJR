def calculate(expression: str):
    try:
        exp_list = list(expression)
        num1 = []
        num2 = []
        operator = None
        firstnumber = True

        NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        OPERATORS = ["+", "-", "*", "/", "**", "//", "%"]

        count = 0

        for elem in exp_list:
            if elem == " ":
                continue

            elif elem == "-" and count == 0:
                num1.append(elem)

            elif elem == "-" and not firstnumber:
                num2.append(elem)

            elif elem in OPERATORS:
                if elem == "*" and exp_list[count + 1] == "*":
                    operator = "**"
                elif elem == "/" and exp_list[count + 1] == "/":
                    operator = "//"
                else:
                    operator = elem

                firstnumber = False

            elif int(elem) in NUMBERS and firstnumber:
                num1.append(elem)

            elif int(elem) in NUMBERS and not firstnumber:
                num2.append(elem)

            count += 1

        num1 = int("".join(num1))
        num2 = int("".join(num2))

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Infinity"
            else:
                return num1 / num2
        elif operator == "**":
            return num1 ** num2
        elif operator == "//":
            if num2 == 0:
                return "Infinity"
            else:
                return num1 // num2
        elif operator == "%":
            return num1 % num2

    except ValueError as e:
        print(f"\033[31mQJRcalculate Error> Wrong value -> {e}\033[0m")

    except KeyboardInterrupt:
        print("Exiting.")
        exit()

    except Exception as e:
        print(f"\033[31mQJRcalculate Error> Unexpected error -> {e}\033[0m")

# testing

if __name__ == "__main__":
    print("Welcome to QJRcalculate v1.0! Enter 'exit' to exit!")
    while True:
        expr = input(" > ")

        if expr == "exit":
            exit()
        else:
            print(calculate(expr))