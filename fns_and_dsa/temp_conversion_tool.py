
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celcius_value = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celcius_value}°C")
    return

def convert_to_fahrenheit(celsius):
    fahrenheit_value = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius}°C is {fahrenheit_value}°F")
    return


def main():
    temp_value = input("Enter the temperature to convert: ")
    conversion_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    try:
        temp_value = float(temp_value)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return  # exit the function early if input was not a number

    match conversion_choice:
        case 'F':
            convert_to_celsius(temp_value)
            return
        case 'C':
            convert_to_fahrenheit(temp_value)
            return
        case _:
            print("invalid conversion choice")
            return
    return

if __name__ == "__main__":
    main()