# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()   # save current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Show current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt user for days
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
