# ...existing code...
def is_leap_year(year):
    """
    Check whether a given year is a leap year.
    A year is a leap year if:
    - It is divisible by 4 AND
    - If divisible by 100, it must also be divisible by 400
    Args:
        year (int): The year to check
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
# ...existing code...
if __name__ == "__main__":
    try:
        year_input = input("Enter a year: ").strip()
        year = int(year_input)
    except ValueError:
        print("Invalid input. Please enter an integer year.")
    else:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
# ...existing code...