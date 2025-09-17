def main():

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sign = input("Choose the operation (+, -, *, /): ")
    result = ""

    match sign :
        case "+" :
            result = num1 + num2
        case "-" :
            result = num1 - num2
        case "*" :
            result = num1 * num2
        case "/" :
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2

    if result != "":
        print(f"The result is {result}.")
    return

if __name__ == "__main__":
    main()

