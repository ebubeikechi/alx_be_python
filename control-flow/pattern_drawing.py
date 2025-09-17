def main():
    user_input = int(input("Enter the size of the pattern: "))
    counter = user_input

    while counter > 0:
        for i in range(1, user_input + 1, 1):
            print("*",end="")

        counter -= 1 
        print("")


if __name__ == "__main__":
    main()
