from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date():
    no_of_days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=no_of_days_to_add)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
    return

def main():
    
    current_date = display_current_datetime()
    print(f"Current date and time: {current_date}")
    calculate_future_date()
    return

if __name__ == "__main__":
    main()