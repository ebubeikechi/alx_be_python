def main():

    user_input = input("What's the weather like today? (sunny/rainy/cold): ")

    if user_input.lower() == "sunny":

        print('Wear a t-shirt and sunglasses.')

    elif user_input.lower() == "rainy":
        print("Don't forget your umbrella and a raincoat.")

    elif user_input.lower() == "cold":
        print("Make sure to wear a warm coat and a scarf.")

    else :
        print("Sorry, I don't have recommendations for this weather.")

    return

if __name__ == "__main__":

    main()

