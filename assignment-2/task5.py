def _read_int_list(prompt: str):
    """Prompt user until a valid list of integers is entered (comma/space separated)."""
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter at least one number.")
            continue
        parts = s.replace(',', ' ').split()
        try:
            return [int(p) for p in parts]
        except ValueError:
            print("Invalid input. Enter integers separated by spaces or commas.")
def sum_even_odd(numbers):
    """Return (sum_even, sum_odd) for the given list of integers."""
    sum_even = sum(x for x in numbers if x % 2 == 0)
    sum_odd = sum(x for x in numbers if x % 2 != 0)
    return sum_even, sum_odd
def main():
    nums = _read_int_list("Enter integers (separated by space or comma): ")
    even_sum, odd_sum = sum_even_odd(nums)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
if __name__ == "__main__":
    main()
# filepath: c:\Users\sunil\OneDrive\Desktop\AIAPS\assignment-2\task5.py
def _read_int_list(prompt: str):
    """Prompt user until a valid list of integers is entered (comma/space separated)."""
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter at least one number.")
            continue
        parts = s.replace(',', ' ').split()
        try:
            return [int(p) for p in parts]
        except ValueError:
            print("Invalid input. Enter integers separated by spaces or commas.")
def sum_even_odd(numbers):
    """Return (sum_even, sum_odd) for the given list of integers."""
    sum_even = sum(x for x in numbers if x % 2 == 0)
    sum_odd = sum(x for x in numbers if x % 2 != 0)
    return sum_even, sum_odd
def main():
    nums = _read_int_list("Enter integers (separated by space or comma): ")
    even_sum, odd_sum = sum_even_odd(nums)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
if __name__ == "__main__":
    main()