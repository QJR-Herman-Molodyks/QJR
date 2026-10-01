def calc_func():
    print("+ = addition")
    print("- = subtraction")
    print("* = multiplication")
    print("/ = division")
    print("** = exponentiation")
    print("% = modulus")
    print("// = floor division")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, **, %, //): ")

    if operation == "+":
        result = num1 + num2
        print(result)
    elif operation == "-":
        result = num1 - num2
        print(result)
    elif operation == "*":
        result = num1 * num2
        print(result)
    elif operation == "**":
        result = num1 ** num2
        print(result)
    elif operation == "%":
        result = num1 % num2
        print(result)
    elif operation == "//":
        if num2 != 0:
            result = num1 // num2
            print(result)
        else:
            result = "Infinite"
            print(result)
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(result)
        else:
            result = "Infinite"
            print(result)
    else:
        result = "\033[31mError: Invalid operation\033[0m"

if __name__ == "__main__":
    calc_func()